from django import forms

from bookshop.models import Book, Publisher, Genre, Author


class ApiBookForm(forms.ModelForm):
  class Meta:
    model = Book
    exclude = ['slug']
    error_messages = {
      'publisher': {
        'invalid': 'Invalid publisher ID. Id must be an integer value',
        'invalid_pk_value': 'Invalid publisher ID: "%(pk)s". Id must be an integer',
        'invalid_choice': 'Publisher with ID %(value)s does not exists!'
      },
      'genres': {
        'invalid_pk_value': 'Invalid genre ID: "%(pk)s". Id must be an integer',
        'invalid_choice': 'Genre with ID %(value)s does not exists!',
      },
      'published_at': {
        'invalid': 'Invalid date format. Enter date as YYYY-MM-DD'
      }
    }


class ApiGenreForm(forms.ModelForm):
  class Meta:
    model = Genre
    exclude = ['slug']


class ApiAuthorForm(forms.ModelForm):
  class Meta:
    model = Author
    exclude = ['slug']


class ApiPublisherForm(forms.ModelForm):
  class Meta:
    model = Publisher
    exclude = ['slug']
