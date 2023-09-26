from django import forms
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory

from bookshop.models import Book, Publisher, Genre, Author, Customer, Address, Order


class ApiBookForm(forms.ModelForm):
  """
  Form for book creation and modification
  """

  class Meta:
    model = Book
    exclude = ['slug']
    error_messages = {
      'publisher': {
        'invalid': 'Invalid publisher ID. Id must be an integer value',
        'invalid_pk_value': 'Invalid publisher ID: "%(pk)s". Id must be an integer',
        'invalid_choice': 'Publisher with ID %(value)s does not exists!'
      },
      'genres': {
        'invalid_pk_value': 'Invalid genre ID: "%(pk)s". Id must be an integer',
        'invalid_choice': 'Genre with ID %(value)s does not exists!',
      },
      'published_at': {
        'invalid': 'Invalid date format. Enter date as YYYY-MM-DD'
      }
    }


class ApiGenreForm(forms.ModelForm):
  """
  Form for genre creation and modification
  """

  class Meta:
    model = Genre
    exclude = ['slug']


class ApiAuthorForm(forms.ModelForm):
  """
  Form for author creation and modification
  """

  class Meta:
    model = Author
    exclude = ['slug']


class ApiPublisherForm(forms.ModelForm):
  """
  Form for publisher creation and modification
  """

  class Meta:
    model = Publisher
    exclude = ['slug']


class ApiCustomerForm(forms.ModelForm):
  """
  Form for customer creation and modification
  """

  class Meta:
    model = Customer
    fields = '__all__'
    error_messages = {
      'address': {
        'invalid': 'Invalid address ID. Id must be an integer value',
        'invalid_pk_value': 'Invalid address ID: "%(pk)s". Id must be an integer',
        'invalid_choice': 'Address with ID %(value)s does not exists!'
      },
      'orders': {
        'invalid_pk_value': 'Invalid order ID: "%(pk)s". Id must be an integer',
        'invalid_choice': 'Order with ID %(value)s does not exists!',
      },
    }

  orders = forms.CharField()

  def __init__(self, *args, **kwargs):
    super(ApiCustomerForm, self).__init__(*args, **kwargs)
    self.fields['orders'] = forms.MultipleChoiceField(
      choices=((order.id, order) for order in Order.objects.all()),
      required=False
    )

  def save(self, *args, **kwargs):
    customer = super(ApiCustomerForm, self).save(*args, **kwargs)
    orders = self.cleaned_data.get('orders')

    if orders is not None:
      customer.orders.set(Order.objects.filter(id__in=orders), clear=True)
      customer.save()

    return customer

  def clean_password(self) -> str:
    """ Validate length and hash given password """
    password = self.cleaned_data['password']

    if len(password) >= 8:
      return make_password(password)
    else:
      raise ValidationError('Password too short! Minimum 8 characters long.')


class ApiAddressForm(forms.ModelForm):
  """
  Form for customer creation and modification
  """

  class Meta:
    model = Address
    fields = '__all__'


class ApiOrderForm(forms.ModelForm):
  """
  Form for order creation and modification
  """

  class Meta:
    model = Order
    fields = '__all__'
