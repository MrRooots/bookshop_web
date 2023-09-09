from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

from bookshop.views import ProductView, BookCreationView

urlpatterns = [
  path('', lambda x: render(x, 'base.html')),

  path('genre/', lambda x: HttpResponse('')),
  path('genre/<int:slug>', lambda x, slug: HttpResponse(f'Genre id: {slug}')),

  path('books/', ProductView.as_view(), name='all_books'),
  path('books/create', BookCreationView.as_view(), name='book_create_url'),
  path('product/<int:slug>', lambda x, slug: HttpResponse(f'Book id: {slug}')),

]
