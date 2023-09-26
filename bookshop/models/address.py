from django.db import models
from django.forms import model_to_dict


class Address(models.Model):
  """
  Address model
  """

  city = models.CharField(max_length=255, null=True)
  street = models.CharField(max_length=255, null=True)
  building_number = models.PositiveSmallIntegerField(null=True)
  apartment = models.PositiveSmallIntegerField(null=True)

  def to_json(self, to_id: bool = False) -> dict:
    """ Convert model to json object """
    return model_to_dict(self)
