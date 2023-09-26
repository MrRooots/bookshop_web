from django.db import models
from django.forms import model_to_dict


class Customer(models.Model):
  """
  Customer model
  """
  first_name = models.CharField(max_length=128, db_index=True)
  last_name = models.CharField(max_length=128, db_index=True)
  email = models.EmailField(max_length=254, db_index=True, unique=True)
  password = models.CharField(max_length=128)
  addresses = models.ManyToManyField('Address', related_name='customer',
                                     blank=True)

  @property
  def get_orders(self) -> list:
    """ Get customer orders list """
    return self.orders.all() if self.orders else []

  def to_json(self, to_id: bool = False) -> dict:
    """ Convert model to json object """
    customer = model_to_dict(self)

    if not to_id:
      customer['addresses'] = [address.to_json() for address in self.addresses.all()]
      customer['orders'] = [order.to_json() for order in self.orders.all()]
    else:
      customer['orders'] = [order.id for order in self.orders.all()]

    return customer

  def __str__(self) -> str:
    return f'({self.id}) {self.first_name} {self.last_name}'
