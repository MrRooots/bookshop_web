from api.forms import ApiAuthorForm, ApiGenreForm, ApiPublisherForm, ApiBookForm
from api.mixins import ApiMultipleObjectsMixin, ApiSingleObjectMixin, ApiObjectsWhereMixin

from bookshop.models import Author, Genre, Publisher, Book


class ApiBooksListView(ApiMultipleObjectsMixin):
  """
  Views for list of books
  """
  model = Book
  form = ApiBookForm


class ApiBookDetailsView(ApiSingleObjectMixin):
  """
  Views for operations with single book
  """
  model = Book
  form = ApiBookForm


class ApiBooksWhereView(ApiObjectsWhereMixin):
  """
  Views for books selected with query params
  """
  model = Book
  PARAMS = {'title': 'icontains',
            'genres': 'id',
            'authors': 'id',
            'publisher': 'id',
            'description': 'icontains'}


class ApiAuthorsListView(ApiMultipleObjectsMixin):
  """
  Views for list of authors
  """
  model = Author
  form = ApiAuthorForm


class ApiAuthorDetailsView(ApiSingleObjectMixin):
  """
  Views for operations with single author
  """
  model = Author
  form = ApiAuthorForm


class ApiAuthorsWhereView(ApiObjectsWhereMixin):
  """
  Views for authors selected with query params
  """
  model = Author
  PARAMS = {'id': 'iexact',
            'name': 'icontains'}


class ApiGenresListView(ApiMultipleObjectsMixin):
  """
  Views for list of genres
  """
  model = Genre
  form = ApiGenreForm


class ApiGenreDetailsView(ApiSingleObjectMixin):
  """
  Views for operations with single genre
  """
  model = Genre
  form = ApiGenreForm


class ApiGenresWhereView(ApiObjectsWhereMixin):
  """
  Views for authors selected with query params
  """
  model = Genre
  PARAMS = {'id': 'iexact',
            'title': 'icontains'}


class ApiPublishersListView(ApiMultipleObjectsMixin):
  """
  Views for list of publishers
  """
  model = Publisher
  form = ApiPublisherForm


class ApiPublisherDetailsView(ApiSingleObjectMixin):
  """
  Views for operations with single publisher
  """
  model = Publisher
  form = ApiPublisherForm


class ApiPublishersWhereView(ApiObjectsWhereMixin):
  """
  Views for authors selected with query params
  """
  model = Publisher
  PARAMS = {'id': 'iexact',
            'title': 'icontains'}
