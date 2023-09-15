import json

from django.core.serializers import serialize
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
  orders = models.ForeignKey('Order', related_name='customer',
                             on_delete=models.CASCADE, blank=True, null=True)

  @property
  def get_orders(self) -> list:
    """ Get customer orders list """
    return self.orders.objects.all() if self.orders else []

  def to_json(self, to_id: bool = False) -> dict:
    """ Convert model to json object """
    customer = model_to_dict(self)

    if not to_id:
      customer['addresses'] = [model_to_dict(address) for address in self.addresses.all()]
      customer['orders'] = model_to_dict(self.orders) if self.orders else None

    return customer
