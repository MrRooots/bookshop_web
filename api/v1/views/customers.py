import json

from django import views
from django.contrib.auth.hashers import check_password, make_password
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from api.v1.forms import ApiCustomerForm, ApiAddressForm, ApiOrderForm
from api.v1.mixins import ApiListViewMixin, ApiDetailsMixin, ApiFilteringMixin, ApiMultipleFormsMixin, BaseMixin, \
  ApiValidationMixin

from bookshop.models import Customer, Address

""" 
Todo: 
  [@transaction.atomic]: add internal exception  
"""


class ApiCustomersListView(ApiMultipleFormsMixin, ApiListViewMixin):
  """
  Views for list of customers
  """
  model = Customer
  form = ApiCustomerForm

  nested_fields = {
    'addresses': ApiAddressForm,
    'orders': ApiOrderForm
  }


class ApiCustomerDetailsView(ApiMultipleFormsMixin, ApiDetailsMixin):
  """
  Views for operations with single customer
  """
  model = Customer
  form = ApiCustomerForm

  nested_fields = {
    'addresses': ApiAddressForm,
    'orders': ApiOrderForm
  }


class ApiCustomersWhereView(ApiFilteringMixin):
  """
  Views for customers selected with query params
  """
  model = Customer
  PARAMS = {'id': 'iexact',
            'first_name': 'icontains',
            'last_name': 'icontains',
            'email': 'iexact',
            'password': 'exact',
            'address': 'iexact'}


class ApiLoginCustomerView(views.View):
  """
  Views for verifying customer data
  """

  @staticmethod
  def post(request) -> JsonResponse:
    data = json.loads(request.body)
    try:
      password = data.get('password', '')
      customer = Customer.objects.get(email__iexact=data.get('email', ''))

      if check_password(password, customer.password) or password == customer.password:
        return JsonResponse({
          'success': 1,
          'customer': customer.to_json(),
        }, status=200)
    except Customer.DoesNotExist:
      pass

    return JsonResponse({'success': 0}, status=401)


@require_http_methods(['POST'])
def update_password(request, obj_id) -> JsonResponse:
  """ Update customer password """
  data = json.loads(request.body)
  try:
    new_pass = data.get('new', '')
    current = data.get('current', '')
    customer = Customer.objects.get(id=obj_id)

    if len(new_pass) < 8:
      return JsonResponse({
        'success': 0,
        'error_fields': {
          'password': ['Password is too short! Minimal length is 8.']
        },
      }, status=400)

    if check_password(current, customer.password) or current == customer.password:
      customer.password = make_password(new_pass)
      customer.save()

      return JsonResponse({
        'success': 1,
        'customer': customer.to_json(),
      }, status=200)

    return JsonResponse({
      'success': 0,
      'error_fields': {
        'password': ['Current password is invalid!']
      },
    }, status=400)
  except Customer.DoesNotExist:
    pass

  return JsonResponse({'success': 0}, status=401)


@require_http_methods(['POST'])
def add_address(request, obj_id) -> JsonResponse:
  """ Add address to customer """
  data = json.loads(request.body)

  try:
    customer = Customer.objects.get(id=obj_id)
    form = ApiAddressForm(data)  # Todo: check for duplicates

    if form.is_valid():
      customer.addresses.add(form.save())
      customer.save()

      return JsonResponse({
        'success': 1,
        'customer': customer.to_json(),
      }, status=200)

    return JsonResponse({
      'success': 0,
      'error_fields': form.errors,
    }, status=400)
  except Customer.DoesNotExist:
    pass

  return JsonResponse({'success': 0}, status=401)
