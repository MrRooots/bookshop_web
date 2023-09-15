from django.db import models
from django.forms import model_to_dict
from django.utils.text import slugify


class Book(models.Model):
  """
  Book model
  """
  title = models.CharField(max_length=256, db_index=True, blank=False)
  description = models.TextField()
  publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE,
                                related_name='books', null=True, blank=True)
  authors = models.ManyToManyField('Author', related_name='books', blank=True)
  genres = models.ManyToManyField('Genre', related_name='books', blank=True)
  published_at = models.DateField()
  published_count = models.PositiveIntegerField()
  page_number = models.PositiveSmallIntegerField()
  weight = models.FloatField()
  slug = models.SlugField(max_length=256, unique=True)

  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)

  def save(self, *args, **kwargs) -> None:
    super(Book, self).save(*args, **kwargs)

    if not self.slug:
      self.slug = f'{slugify(self.title, allow_unicode=True)}-{self.id}'
      self.save()

  def to_json(self, to_id: bool = False) -> dict:
    book = model_to_dict(self)

    if not to_id:
      book['genres'] = [model_to_dict(genre, exclude=['slug']) for genre in self.genres.all()]
      book['authors'] = [model_to_dict(author, exclude=['slug']) for author in self.authors.all()]

      if self.publisher:
        book['publisher'] = model_to_dict(self.publisher, exclude=['slug'])

    return book
