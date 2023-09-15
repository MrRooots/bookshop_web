from django.db import models
from django.forms import model_to_dict
from django.utils.text import slugify


class Genre(models.Model):
  """
  Genre model
  """
  title = models.CharField(max_length=128, db_index=True, blank=False)
  slug = models.SlugField(max_length=128, unique=True)

  def save(self, *args, **kwargs) -> None:
    super(Genre, self).save(*args, **kwargs)

    if not self.slug:
      self.slug = f'{slugify(self.title, allow_unicode=True)}-{self.id}'
      self.save()

  def to_json(self) -> dict:
    return model_to_dict(self, exclude=['slug'])
