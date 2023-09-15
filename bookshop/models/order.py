from django.db import models


class Order(models.Model):
  """
  Order model
  """

  class OrderStatus(models.IntegerChoices):
    CANCELED = 0
    PLACED = 1
    IN_DELIVERY = 2
    DELIVERED = 3
    DELAYED = 4

  date = models.DateField(auto_now_add=True)
  shipping_method = models.ForeignKey('ShippingMethod', related_name='orders',
                                      on_delete=models.CASCADE)
  destination_address = models.ForeignKey('Address', related_name='orders',
                                          on_delete=models.CASCADE)
  books = models.ManyToManyField('Book', related_name='orders')
  price = models.FloatField()
  status = models.PositiveSmallIntegerField(choices=OrderStatus.choices)
