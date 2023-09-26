from django.db import models
from django.forms import model_to_dict


class ShippingMethod(models.Model):
  """
  Shipping method model
  """
  name = models.CharField(max_length=128, db_index=True)
  cost = models.FloatField()

  def to_json(self, to_id: bool = False) -> dict:
    """ Convert model to json object """
    return model_to_dict(self)
