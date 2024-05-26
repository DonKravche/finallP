Django Library Management System
This is a web application built with Django that allows library staff to manage the book catalog, track book issues and returns, and provides users with the ability to register and access library services.
Features
User Registration

Users can register on the site by providing their email, password, full name, personal number, birth date, and other required information.
Library staff can be added to the site through the admin panel.

Authentication

Both library staff and registered users can log in to the site.

Book Management

Library staff can add, delete, and update book information through the Django admin interface and via API (for external systems).
The system includes at least 1000 randomly generated books.
Each book has the following information:

Title
Author (separate model with appropriate fields)
Genre (separate model with appropriate fields)
Publication date
Stock quantity


The admin interface provides filtering and search functionality for managing the book list.
For each book in the admin interface, library staff can view:

Number of times the book has been issued
Current availability (whether the book can be issued or not)
Number of copies currently issued
History of book issues and returns (who checked out the book and when it was returned)



User-side Book List and Details

Registered users can view a list of books and detailed information through an API.
The book list includes filtering, searching, and pagination functionality.
Users can reserve an available book for one day. The reservation is automatically removed if the book is not checked out.
Library staff can mark in the database when a user returns a book.

Statistics

An API endpoint provides statistical data:

Top 10 most popular (most requested) books
Number of times each book was checked out from the library in the last year
Top 100 books that were most often returned late
Top 100 users who most often returned books late



Technologies Used

Django
Django REST Framework (for building the RESTful API)
(Optional) Template rendering library or Qt library for the user interface

Installation and Setup

Clone the repository: git clone https://github.com/your-repo/library-management.git
Navigate to the project directory: cd library-management
Create a virtual environment: python -m venv env
Activate the virtual environment:

On Windows: env\Scripts\activate
On Unix or macOS: source env/bin/activate


Install the required packages: pip install -r requirements.txt
Run database migrations: python manage.py migrate
Create a superuser for the admin interface: python manage.py createsuperuser
Start the development server: python manage.py runserver

Usage

Access the admin interface at http://localhost:8000/admin to manage books, authors, genres, and library staff.
Access the API endpoints for user registration, authentication, book listing, reservation, and statistics.
(Optional) Use the provided user interface to interact with the library management system.

Contributing
Contributions are welcome! Please follow these steps:

Fork the repository
Create a new branch: git checkout -b feature/your-feature
Make your changes and commit them: git commit -m 'Add your feature'
Push to the branch: git push origin feature/your-feature
Submit a pull request

License
This project is licensed under the MIT License.
