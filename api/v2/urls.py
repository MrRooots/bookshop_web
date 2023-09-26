from django.http import JsonResponse
from django.urls import path

urlpatterns = [
  path('', lambda request: JsonResponse({
    'success': 0, 'message': 'Under Development'
  }, status=404)),
]
