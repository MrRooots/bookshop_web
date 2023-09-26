from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('bookshop.urls')),

  # Pure Django API
  path('api/v1/', include('api.v1.urls')),

  # API build with Django Rest Framework
  path('api/v2/', include('api.v2.urls')),
]
