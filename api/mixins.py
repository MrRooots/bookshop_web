import json

from django import views
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse


class BaseMixin(views.View):
  """
  Base mixins class
  """
  model = None
  form = None
  PARAMS: dict = None


class ApiMultipleObjectsMixin(BaseMixin):
  """
  Base class for list view of objects.

  In case of nested objects in JSON override _save_form method.
  """

  def _save_form(self, data: dict) -> tuple:
    """ Base save form method for single form """
    obj, errors = None, None
    form = self.form(data)

    if form.is_valid():
      obj = form.save()
    else:
      errors = form.errors

    return obj, errors

  def get(self, request) -> JsonResponse:
    """ Get list of objects """
    limit, offset = map(int, (request.GET.get('limit', 20),
                              request.GET.get('offset', 0)))
    objects = self.model.objects.all()[offset:offset + limit]

    return JsonResponse({
      'success': 1,
      'count': objects.count(),
      'result': [obj.to_json() for obj in objects],
    }, status=200)

  def post(self, request, *args, **kwargs) -> JsonResponse:
    """ Create new object """
    try:
      obj, errors = self._save_form(json.loads(request.body))
      if obj:
        return JsonResponse({
          'success': 1,
          'result': obj.to_json(),
        }, status=200)
      else:
        return JsonResponse({
          'success': 0,
          'error_fields': errors,
        }, status=400)
    except (json.JSONDecodeError, KeyError):
      return JsonResponse({
        'success': 0,
        'error_fields': {'json': ['Invalid input json.']},
      }, status=400)


class ApiSingleObjectMixin(BaseMixin):
  """
  Base class for operations with single object

  In case of nested objects in JSON override _save_form method.
  """

  def _save_form(self, data: dict, instance) -> tuple:
    """ Save form """
    obj, errors = None, None
    form = self.form(data, instance=instance)

    if form.is_valid():
      obj = form.save()
    else:
      errors = form.errors

    return obj, errors

  def get(self, request, obj_id: int) -> JsonResponse:
    """ Get specific object """
    try:
      return JsonResponse({
        'success': 1,
        'result': self.model.objects.get(id=obj_id).to_json()
      }, status=200)
    except ObjectDoesNotExist:
      return JsonResponse({
        'success': 0,
        'error': f'{self.model.__name__} with id {obj_id} does not exists!'
      }, status=404)

  def patch(self, request, obj_id: int) -> JsonResponse:
    """ Update specific object """
    try:
      data = json.loads(request.body)
      obj = self.model.objects.get(id=obj_id)

      # Persist fields that are not in POST
      data.update({k: v for k, v in obj.to_json(to_id=True).items()
                   if k not in data})
      new_obj, errors = self._save_form(data, obj)

      if new_obj:
        return JsonResponse({
          'success': 1,
          'result': new_obj.to_json(),
        }, status=200)
      else:
        return JsonResponse({
          'success': 0,
          'error_fields': errors,
        }, status=400)
    except ObjectDoesNotExist:
      return JsonResponse({
        'success': 0,
        'error': f'{self.model.__name__} with id {obj_id} does not exists!'
      }, status=404)

  def delete(self, request, obj_id: int) -> JsonResponse:
    """ Delete specific object """
    try:
      self.model.objects.get(id=obj_id).delete()

      return JsonResponse({
        'success': 1,
      }, status=200)
    except ObjectDoesNotExist:
      return JsonResponse({
        'success': 0,
        'error': f'{self.model.__name__} with id {obj_id} does not exists!'
      }, status=404)


class ApiObjectsWhereMixin(BaseMixin):
  """
  Base class for operations with list of filtered objects
  """

  def _get_filters(self, params) -> dict:
    """ Get filters from query params """
    return {
      '{0}__{1}'.format(param, self.PARAMS[param]): val
      for param, val in params.items()
      if param in self.PARAMS
    }

  def get(self, request) -> JsonResponse:
    filters = self._get_filters(request.GET)
    objects = self.model.objects.filter(**filters)

    return JsonResponse({
      'success': 1,
      'request': filters,
      'count': objects.count(),
      'result': [obj.to_json() for obj in objects]
    }, status=200)
