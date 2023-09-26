from django.db import models
from django.forms import model_to_dict


class Order(models.Model):
  """
  Order model
  """

  class OrderStatus(models.IntegerChoices):
    CANCELED = 0, 'Canceled'
    PLACED = 1, 'Placed'
    IN_DELIVERY = 2, 'In delivery'
    DELIVERED = 3, 'Delivered'
    DELAYED = 4, 'Delayed'

  date = models.DateField(auto_now_add=True)
  shipping_method = models.ForeignKey('ShippingMethod', related_name='orders',
                                      on_delete=models.CASCADE)
  destination_address = models.ForeignKey('Address', related_name='orders',
                                          on_delete=models.CASCADE)
  books = models.ManyToManyField('Book', related_name='orders', blank=True)
  price = models.FloatField()
  status = models.PositiveSmallIntegerField(choices=OrderStatus.choices)
  customer = models.ForeignKey('Customer', related_name='orders',
                               on_delete=models.CASCADE, blank=True, null=True)

  def to_json(self, to_id: bool = False) -> dict:
    """ Convert model to json object """
    order = model_to_dict(self)

    if not to_id:
      order['destination_address'] = self.destination_address.to_json()
      order['shipping_method'] = self.shipping_method.to_json()

    return order
