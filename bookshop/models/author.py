from django.db import models
from django.utils.text import slugify


class Author(models.Model):
  """
  Author model
  """
  name = models.CharField(max_length=128, db_index=True, blank=False)
  slug = models.SlugField(max_length=128, unique=True)

  def save(self, *args, **kwargs) -> None:
    super(Author, self).save(*args, **kwargs)

    if not self.slug:
      self.slug = f'{slugify(self.name, allow_unicode=True)}-{self.id}'
      self.save()

  def to_json(self) -> dict:
    return {
      'id': self.id,
      'title': self.name
    }
