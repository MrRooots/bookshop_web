from django.db import models


class ShippingMethod(models.Model):
  """
  Shipping method model
  """
  name = models.CharField(max_length=128, db_index=True)
  cost = models.FloatField()
