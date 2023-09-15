from api.forms import ApiCustomerForm, ApiAddressForm
from api.mixins import ApiMultipleObjectsMixin, ApiSingleObjectMixin, ApiObjectsWhereMixin

from bookshop.models import Customer, Address


class ApiCustomersListView(ApiMultipleObjectsMixin):
  """
  Views for list of customers
  """
  model = Customer
  form = ApiCustomerForm

  nested_field = 'address'
  nested_form = ApiAddressForm

  def _save_form(self, data: dict) -> tuple:
    obj, errors, address_form = None, None, None

    if data.get(self.nested_field) and isinstance(data[self.nested_field], dict):
      address_form = self.nested_form(data[self.nested_field])
      del data[self.nested_field]

    form = self.form(data)

    if form.is_valid():
      obj = form.save()

      if address_form is not None:
        if address_form.is_valid():
          obj.addresses.set([address_form.save()], clear=True)
          obj.save()
        else:
          errors = address_form.errors
    else:
      errors = form.errors

    return obj, errors


class ApiCustomerDetailsView(ApiSingleObjectMixin):
  """
  Views for operations with single customer
  """
  model = Customer
  form = ApiCustomerForm


class ApiCustomersWhereView(ApiObjectsWhereMixin):
  """
  Views for customers selected with query params
  """
  model = Customer
  PARAMS = {'id': 'iexact',
            'first_name': 'icontains',
            'last_name': 'icontains',
            'email': 'iexact',
            'address': 'iexact'}


class ApiCustomerAddressListView(ApiMultipleObjectsMixin):
  """
  Views for list of customer addresses
  """
  model = Address
  form = ApiAddressForm


class ApiCustomerAddressDetailsView(ApiSingleObjectMixin):
  """
  Views for operations with single customer address
  """
  model = Address
  form = ApiAddressForm
