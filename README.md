# Django To-Do List Project

## Project Overview
This is a Django-based **To-Do List** web application, organized with **Clean Architecture** principles. The application is designed for modularity, easy testing, and flexibility, allowing for future growth and maintainability.

## Key Concepts

### Clean Architecture
The project follows **Clean Architecture** to separate different layers of the application, which promotes testability, scalability, and maintainability. The layers are organized as follows:

The dependencies must follow this order: `Entities` <- `Domain` <- `Application` <- `Infrastructure`.

See the `src` README.md files for details.

### How to run

Start the server: `python manage.py runserver`

