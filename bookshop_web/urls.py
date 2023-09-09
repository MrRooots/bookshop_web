from django.http import HttpResponse, JsonResponse
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('bookshop.urls')),

  # path('shop/', include('bookshop.urls')),

  path('api/', include('api.urls'))
]
