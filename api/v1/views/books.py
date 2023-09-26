from api.v1.forms import ApiAuthorForm, ApiGenreForm, ApiPublisherForm, ApiBookForm
from api.v1.mixins import ApiListViewMixin, ApiDetailsMixin, ApiFilteringMixin

from bookshop.models import Author, Genre, Publisher, Book


class ApiBooksListView(ApiListViewMixin):
  """
  Views for list of books
  """
  model = Book
  form = ApiBookForm


class ApiBookDetailsView(ApiDetailsMixin):
  """
  Views for operations with single book
  """
  model = Book
  form = ApiBookForm


class ApiBooksWhereView(ApiFilteringMixin):
  """
  Views for books selected with query params
  """
  model = Book
  PARAMS = {'title': 'icontains',
            'genres': 'id',
            'authors': 'id',
            'publisher': 'id',
            'description': 'icontains'}


class ApiAuthorsListView(ApiListViewMixin):
  """
  Views for list of authors
  """
  model = Author
  form = ApiAuthorForm


class ApiAuthorDetailsView(ApiDetailsMixin):
  """
  Views for operations with single author
  """
  model = Author
  form = ApiAuthorForm


class ApiAuthorsWhereView(ApiFilteringMixin):
  """
  Views for authors selected with query params
  """
  model = Author
  PARAMS = {'id': 'iexact',
            'name': 'icontains'}


class ApiGenresListView(ApiListViewMixin):
  """
  Views for list of genres
  """
  model = Genre
  form = ApiGenreForm


class ApiGenreDetailsView(ApiDetailsMixin):
  """
  Views for operations with single genre
  """
  model = Genre
  form = ApiGenreForm


class ApiGenresWhereView(ApiFilteringMixin):
  """
  Views for authors selected with query params
  """
  model = Genre
  PARAMS = {'id': 'iexact',
            'title': 'icontains'}


class ApiPublishersListView(ApiListViewMixin):
  """
  Views for list of publishers
  """
  model = Publisher
  form = ApiPublisherForm


class ApiPublisherDetailsView(ApiDetailsMixin):
  """
  Views for operations with single publisher
  """
  model = Publisher
  form = ApiPublisherForm


class ApiPublishersWhereView(ApiFilteringMixin):
  """
  Views for authors selected with query params
  """
  model = Publisher
  PARAMS = {'id': 'iexact',
            'title': 'icontains'}
