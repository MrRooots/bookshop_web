import json

from django import views
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse

from api.v1.forms import ApiCustomerForm, ApiAddressForm, ApiOrderForm
from api.v1.mixins import ApiListViewMixin, ApiDetailsMixin, ApiFilteringMixin, ApiMultipleFormsMixin, BaseMixin, \
  ApiValidationMixin

from bookshop.models import Customer

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
        })
    except Customer.DoesNotExist:
      pass

    return JsonResponse({'success': 0}, status=401)
