from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from api.views import *

urlpatterns = [
  path('', ApiBooksListView.as_view()),

  path('books/', csrf_exempt(ApiBooksListView.as_view())),
  path('books/where', csrf_exempt(ApiBooksWhereView.as_view())),
  path('books/<int:obj_id>', csrf_exempt(ApiBookDetailsView.as_view())),

  path('authors/', csrf_exempt(ApiAuthorsListView.as_view())),
  path('authors/where', csrf_exempt(ApiAuthorsWhereView.as_view())),
  path('authors/<int:obj_id>', csrf_exempt(ApiAuthorDetailsView.as_view())),

  path('genres/', csrf_exempt(ApiGenresListView.as_view())),
  path('genres/where', csrf_exempt(ApiGenresWhereView.as_view())),
  path('genres/<int:obj_id>', csrf_exempt(ApiGenreDetailsView.as_view())),

  path('publishers/', csrf_exempt(ApiPublishersListView.as_view())),
  path('publishers/where', csrf_exempt(ApiPublishersWhereView.as_view())),
  path('publishers/<int:obj_id>', csrf_exempt(ApiPublisherDetailsView.as_view())),

  path('customers/', csrf_exempt(ApiCustomersListView.as_view())),
  path('customers/where', csrf_exempt(ApiCustomersWhereView.as_view())),
  path('customers/address', csrf_exempt(ApiCustomerAddressListView.as_view())),
  path('customers/<int:obj_id>', csrf_exempt(ApiCustomerDetailsView.as_view())),

  path('customers/<int:obj_id>/addresses/<int:addr_id>', csrf_exempt(ApiCustomerAddressDetailsView.as_view())),
]
