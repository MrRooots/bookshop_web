from django import forms
from django.core.exceptions import ValidationError

from bookshop.models import Book, Author, Genre


class BookForm(forms.ModelForm):
  class Meta:
    model = Book
    fields = ['title',
              'description',
              'published_at',
              'page_number',
              'published_count',
              'weight',
              'slug', ]
    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      'description': forms.TextInput(attrs={'class': 'form-control'}),
      'published_at': forms.TextInput(attrs={'class': 'form-control'}),
      'page_number': forms.TextInput(attrs={'class': 'form-control'}),
      'published_count': forms.TextInput(attrs={'class': 'form-control'}),
      'weight': forms.TextInput(attrs={'class': 'form-control'}),
      'slug': forms.TextInput(attrs={'class': 'form-control'}),
    }

  def clean_slug(self):
    new_slug = self.cleaned_data['slug'].lower()

    if new_slug == 'create':
      raise ValidationError('Slug may not be created')

    if Book.objects.filter(slug__iexact=new_slug).count():
      raise ValidationError('Slug "{}" is already exist. Slug have to be unique!'.format(new_slug))

    return new_slug

# # Сздание поста через html форму
# class PostForm(forms.ModelForm):
#   class Meta:
#     model = Post
#     fields = ['title', 'slug', 'body', 'tags']
#     widgets = {
#       'title': forms.TextInput(attrs={'class': 'form-control'}),
#       'slug': forms.TextInput(attrs={'class': 'form-control'}),
#       'body': forms.Textarea(attrs={'class': 'form-control'}),
#       'tags': forms.SelectMultiple(attrs={'class': 'form-control'})
#     }
#
#   def clean_slug(self):
#     new_slug = self.cleaned_data['slug'].lower()
#
#     # if new_slug == 'create':
#     #    raise ValidationError('Slug may not be created')
#     # return new_slug
#
#     return new_slug if new_slug != 'create' else ValidationError('Slug may not be created')
