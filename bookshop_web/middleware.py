from django.http import HttpResponse, JsonResponse

from django.conf import settings


class ApiAuthMiddleware:
  """
  Middleware to control API errors in JSON format
  """

  def __init__(self, get_response) -> None:
    self.get_response = get_response

  def __call__(self, request):
    response = self.get_response(request)

    if '/api/' in request.path:
      if request.headers.get('API-KEY', '') != settings.API_KEY or response.status_code == 401:
        return JsonResponse({
          'success': 0,
          'error': '401 Unauthorized'
        }, status=401)
      elif response.status_code == 404:
        return JsonResponse({
          'success': 0,
          'error': '404 Not Found'
        }, status=404)
      elif response.status_code == 405:
        return JsonResponse({
          'success': 0,
          'error': '405 Method Not Allowed'
        }, status=405)
      elif response.status_code == 405:
        return JsonResponse({
          'success': 0,
          'error': '400 Bad Request'
        }, status=400)

    return response
