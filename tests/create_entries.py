import random

import requests

BASE_URL = 'http://localhost:8000/api'
session = requests.Session()
session.headers = {'API-KEY': 'SUPERSECRET_APIKEY'}


def create_books():
  with open('data/books.in', 'r') as file:
    while line := file.readline():
      line = line.split(', ')
      session.post(f'{BASE_URL}/books/', json={
        "title": line[0],
        "description": line[1],
        "published_at": line[2],
        "genres": [
          *random.sample([2, 3, 4, 5, 6, 7], random.randint(1, 5))
        ],
        "page_number": line[3],
        "published_count": line[4],
        "weight": line[5],
        "publisher": line[6],
      })


def create_publishers():
  for title in ('AST', 'Eksmo', 'Bombora'):
    session.post(f'{BASE_URL}/publishers/', json={
      'title': title
    })


def create_genres():
  for title in ('Classic literature', 'Artistic literature',
                'Fiction', 'Tales', 'Comics', 'Cooking'):
    session.post(f'{BASE_URL}/genres/', json={
      'title': title
    })


def create_authors():
  for name in ('William Shakespeare', 'Jane Austen', 'Charles Dickens',
               'Leo Tolstoy', 'Fyodor Dostoevsky', 'Mark Twain',
               'Charlotte Bronte', 'George Orwell', 'Ernest Hemingway',
               'Edgar Allan Poe',):
    session.post(f'{BASE_URL}/authors/', json={
      'name': name
    })


def create_entries():
  create_publishers()
  create_authors()
  create_genres()
  create_books()


if __name__ == '__main__':
  create_entries()
