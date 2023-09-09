from django.db import models
from django.utils.text import slugify


class Book(models.Model):
  """
  Book model
  """
  title = models.CharField(max_length=256, db_index=True, blank=False)
  description = models.TextField()
  publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE,
                                blank=True, related_name='books', null=True)
  authors = models.ManyToManyField('Author', blank=True, related_name='books')
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
    genres = [genre.id if to_id else genre.to_json() for genre in self.genres.all()]
    authors = [author.id if to_id else author.to_json() for author in self.authors.all()]
    publisher = self.publisher.id if to_id else self.publisher.to_json() if self.publisher else ''

    return {
      'id': self.id,

      'title': self.title,
      'description': self.description,
      'authors': authors,
      'genres': genres,

      'publisher': publisher,
      'published_at': self.published_at,
      'published_count': self.published_count,

      # 'slug': self.slug,
      'weight': self.weight,
      'page_number': self.page_number,
    }
