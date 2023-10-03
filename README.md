


# Ticket Management System

The Ticket Management System is a Django-based web application designed for managing and tracking tickets, user feedback, and user profiles with various roles (company, technician, dispatcher).

## Project Structure

### Directory Structure

The project directory structure is organized as follows:

- `Ticket_App/` (main app directory)
  - `models.py`: Defines the database models, including `SystemUser` (with roles), `Ticket`, and `Feedback`.
  - `admin.py`: Registers the models with the Django admin panel.
  - `forms.py`: Contains forms for linking models to views.
  - `views.py`: Defines view functions for handling user interactions and operations.
  - `decorators.py`: Contains custom decorators for validating user roles.
  - `urls.py`: Defines URL patterns and routes.
  - `migrations/`: Stores database migration files.

- `static/`: Contains static files such as CSS, JavaScript, and images.

- `templates/`: Contains HTML templates organized into directories:
  - `form/`: Contains registration forms for users, tickets, and feedback.
  - `updates/`: Contains user profile and ticket update templates.
  - `login/`: Contains login form templates.
  - `lists/`: Contains HTML templates for listing models (users, tickets, feedback).
  - `details/`: Contains HTML templates for displaying individual model details.
  - `base.html`: Base template used as the layout for other pages.
  - `home.html`: Home page template.
  - `about.html`: About page template.

### User Roles

- **Company**: Represents a company user role.
- **Technician**: Represents a technician user role.
- **Dispatcher**: Represents a dispatcher user role.



### Made use of free images from the following websites:

    bootstrap icons
    https://www.streamlinehq.com/
    https://www.freepik.com


### Usage:

    - Due to advice provided on the ALX Software Engineering programme I have removed some comment regarding running this project locally on any machine.
    - Visit the home page to get started with the Ticket Management System.
    - Use the registration forms to create new user accounts with different roles.
    - An admin user can access the admin panel at `/admin/` to manage users, tickets, and feedback.
    - Utilize the various HTML templates for listing and viewing details of users, tickets, and feedback.
