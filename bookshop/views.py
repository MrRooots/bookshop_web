from django import views
from django.http import HttpResponse
from django.shortcuts import render

# Create your views__ here.
from bookshop.forms import BookForm
from bookshop.models import Book, Publisher


class ProductView(views.View):
  """
  Product view
  """

  @staticmethod
  def get(request) -> HttpResponse:
    books = Book.objects.all()

    return render(request, 'bookshop/index.html', context={
      'books': books
    })


class CategoryView(views.View):
  @staticmethod
  def get(request) -> HttpResponse:
    return render(request, 'bookshop/index.html', context={

    })


class BookCreationView(views.View):
  @staticmethod
  def get(request) -> HttpResponse:
    form = BookForm()
    publishers = Publisher.objects.all()

    return render(request, 'bookshop/create_book.html', context={
      'form': form,
      'publishers': publishers
    })

  @staticmethod
  def post(request) -> HttpResponse:
    pass
