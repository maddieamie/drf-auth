# Lab 33: Lab 32 Extension, Django REST API with Permissions and PostgreSQL

## Author: Maddie Amelia Lewis

### Overview

This project creates a **Django REST Framework (DRF)** API that restricts access to data for magical creatures, using a PostgreSQL database running in **Docker**. Permissions are adjusted so that only authenticated users can access the API. Additionally, custom permissions are implemented to allow only the owners of the magical creatures to update or delete them.

### Feature Tasks and Requirements

#### Features - General
- The project demonstrates how to restrict access to portions of the API data.
- The project uses PostgreSQL instead of SQLite as the database.
- The functionality of two demos has been merged into this project.

#### Features - Django REST Framework
- The site is a **DRF-powered API**.
- Permissions are set so that only **authenticated users** can access the API.
- Custom permissions restrict updates and deletions to the **owner** of a magical creature.
- The API provides the ability to switch users directly from the browsable API.

#### Features - Docker
- A **Dockerfile** based on `python:3.10-slim` is created to run the Django app as a web service.
- A **docker-compose.yml** is included to manage both the Django app and PostgreSQL as services.
- The app can be started with `docker compose up --build`.
- PostgreSQL is used as the database service.

#### Implementation Notes
- PostgreSQL runs inside Docker; no local PostgreSQL installation is needed.
- All operations like `createsuperuser` and `migrate` are executed inside the container using Docker commands.
- Example Docker commands:
    - `docker compose run web python manage.py migrate`
    - `docker compose run web python manage.py createsuperuser`

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/drf-api-permissions-postgres.git
   cd drf-api-permissions-postgres
2. Build and start the Docker containers:

`docker compose up --build`
3. Run migrations:

`docker compose run web python manage.py migrate`

4. Create a superuser:

`docker compose run web python manage.py createsuperuser`

5. Access the API at http://localhost:8000/api/api/creatures/.


**Docker Commands**

1. Start the app and PostgreSQL services:

`docker compose up`

2. Run a management command inside the container:


`docker compose run web python manage.py <command>`

3. Rebuild the container after changes:


`docker compose up --build`


### Database Setup

The database is configured using PostgreSQL, running in a Docker container. The database credentials are stored in the docker-compose.yml file as environment variables.

PostgreSQL Settings (inside docker-compose.yml)

**API Overview**

Endpoints:
- `/api/creatures/` - List or create magical creatures (GET, POST).
- `/api/creatures/<id>/` - Retrieve, update, or delete a magical creature (GET, PUT, PATCH, DELETE).

**Permissions:**
Authenticated users can view and create magical creatures.
Only the owner of a magical creature can update or delete it.


### Tests
To run tests:


`docker compose run web python manage.py test`

**User Acceptance Tests**


Adjust tests provided in the demo to verify that all project features work as expected.
Ensure tests cover permission-based access to the API.