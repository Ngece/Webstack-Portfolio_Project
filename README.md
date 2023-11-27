# Ticket Management System - Django Web Application

## Introduction

Welcome to the Ticket Management System, a robust Django-based web application designed for efficient ticket management, user feedback, and user profiles with distinct roles such as company, technician, and dispatcher.

## Project Structure

### Directory Structure

The project directory structure is meticulously organized to enhance readability and maintainability:

- **Ticket_App/** (main app directory)
  - `models.py`: Defines database models, including SystemUser (with roles), Ticket, and Feedback.
  - `admin.py`: Registers models with the Django admin panel.
  - `forms.py`: Contains forms for linking models to views.
  - `views.py`: Defines view functions for user interactions and operations.
  - `decorators.py`: Contains custom decorators for validating user roles.
  - `urls.py`: Defines URL patterns and routes.
  - `migrations/`: Stores database migration files.

- **static/**: Contains static files such as CSS, JavaScript, and images.

- **templates/**: Contains HTML templates organized into directories:
  - `form/`: Holds registration forms for users, tickets, and feedback.
  - `updates/`: Contains user profile and ticket update templates.
  - `login/`: Holds login form templates.
  - `lists/`: Contains HTML templates for listing models (users, tickets, feedback).
  - `details/`: Contains HTML templates for displaying individual model details.
  - `base.html`: Base template used as the layout for other pages.
  - `home.html`: Home page template.
  - `about.html`: About page template.

## User Roles

- **Company:** Represents a company user role.
- **Technician:** Represents a technician user role.
- **Dispatcher:** Represents a dispatcher user role.

## Acknowledgments

Made use of free images from the following websites:

- [Bootstrap Icons](https://icons.getbootstrap.com/)
- [Streamline Icons](https://www.streamlinehq.com/)
- [Freepik](https://www.freepik.com)

## Getting Started

### Prerequisites
- Ensure you have Python and Django installed on your system.

## How to run the project
1. Install dependencies:
  pip install -r requirements.txt
2. Apply migrations:
  python manage.py migrate
3. Run the development server:
  python manage.py runserver
Navigate to http://127.0.0.1:8000/

#Usage

    #User Registration:
        Companies, technicians, and dispatchers can register using the provided forms.

    #Login and Logout:
        Users can securely log in and out, with appropriate messages displayed for feedback.

    #Ticket Creation:
        Companies can create new tickets, which are initially in a pending state.

    #Ticket Approval:
        Dispatchers can approve or reject tickets, influencing the workflow.

    #Ticket Assignment:
        Technicians can accept tickets, marking them as accepted and proceed with monitoring or closing.

    #Feedback Submission:
        Users can submit feedback on their experiences.

    #Feedback Management:
        Dispatchers have control over posted feedback, deciding whether to display it on the home page.

    #Profile Updates:
        Users can update their profiles as needed.

Feel free to explore the various features and functionalities of the Ticket Management System.
#Contributors
    Josaya Ngece

Checkout the project functionality on my youtube channel: https://www.youtube.com/watch?v=G97DTkFId9k
