# Bookshop API V1

### Powered with pure Django

# Functionality

**books/**

- GET: Get list of books
- POST: Add new book

**books/where**

- GET: Get filtered books

**books/\<int:obj_id>**

- GET: Get information about concrete book
- PATCH: Update concrete book
- DELETE: Delete concrete book

The following URLs have the same functionality:

- **authors/**, **genres/**, **publishers/**