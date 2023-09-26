from api.v1.forms import ApiCustomerForm, ApiAddressForm, ApiOrderForm
from api.v1.mixins import ApiListViewMixin, ApiDetailsMixin, ApiFilteringMixin, ApiMultipleFormsMixin

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
            'address': 'iexact'}
