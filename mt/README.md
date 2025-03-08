# Django Project - mt

This is a Django project named **mt** designed for managing a reservation system. The project includes three main applications: **customers**, **tables**, and **reservations**.

## Project Structure

- **manage.py**: Command-line utility for managing the Django project.
- **mt/**: Contains the main project settings and configurations.
  - **settings.py**: Project settings including database configurations and installed apps.
  - **urls.py**: URL routing for the project.
  - **wsgi.py**: WSGI deployment configuration.
  - **asgi.py**: ASGI deployment configuration.
- **customers/**: Application for managing customer data.
  - **models.py**: Defines the Customer model.
  - **views.py**: Handles customer-related requests.
  - **admin.py**: Registers the Customer model with the admin site.
- **tables/**: Application for managing tables.
  - **models.py**: Defines the Table model.
  - **views.py**: Handles table-related requests.
  - **admin.py**: Registers the Table model with the admin site.
- **reservations/**: Application for managing reservations.
  - **models.py**: Defines the Reservation model.
  - **views.py**: Handles reservation-related requests.
  - **admin.py**: Registers the Reservation model with the admin site.
- **templates/**: Contains HTML templates for rendering views.
  - **base.html**: Base template for the application.
  - **header.html**: Header template used in the base template.
- **static/**: Contains static files such as CSS, JavaScript, and images.
  - **css/**: CSS files for styling the application using Bootstrap.
  - **js/**: JavaScript files for the application.
  - **images/**: Image files used in the application.

## Features

- Manage customers with the ability to create, retrieve, and list customer information.
- Manage tables with the ability to create and list tables, including checking availability.
- Manage reservations with the ability to create, retrieve, update, and delete reservations, ensuring no double bookings for customers.

## Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required packages using `pip install -r requirements.txt`.
4. Run migrations with `python manage.py migrate`.
5. Start the development server with `python manage.py runserver`.

## Usage

- Access the application at `http://127.0.0.1:8000/`.
- Use the defined endpoints to interact with customers, tables, and reservations.

## License

This project is licensed under the MIT License.