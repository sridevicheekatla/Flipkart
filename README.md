Django Project Documentation

Introduction:
    This document provides a comprehensive guide for setting up a Django project using Docker, integrating PostgreSQL as the database, and implementing various features, including a script for importing data, APIs for product specifications, and models for AllProducts, RegularFit, and RelaxedFit. Additionally, it introduces the Fitlist API for filtering relaxed fit and regular fit based on the type of fit.

Prerequisites:
    Ensure you have Docker installed on your system.
    Familiarity with Django 
    Basic command-line operations.

Project Structure:

    myproj/
    │
    ├── myapp/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations/
    │   ├── models.py
    │   ├── scripts.py
    │   ├── tests.py
    │   └── views.py
    │
    ├── myproj/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    │
    ├── data/
    │   └── db/
    │
    ├── .gitignore
    ├── Dockerfile
    ├── docker-compose.yml
    ├── manage.py
    ├── requirements.txt
    └──flipkart.csv

Django Configuration
    To create project
        command: django-admin startproject <myproj>
    To create app
        Command: python manage.py startapp <myapp>
    Settings
        Include app in the installed app
        Configure the PostgreSQL Django database settings.
    Models
        AllProducts
        RegularFit
        RelaxedFit

Docker Configuration
    Dockerfile
        FROM python:3: Base Docker image.
        ENV PYTHONUNBUFFERED=1: Ensures that Python prints directly to the terminal without buffering.
        WORKDIR /code: Sets the working directory to /code.
        COPY requirements.txt /code/: Copies the requirements file into the container.
        RUN pip install -r requirements.txt: Installs Python dependencies.
        COPY . /code/: Copies the project files into the container.
        CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]: Specifies the default command to run the development server.


docker-compose.yml
    db service: Defines a PostgreSQL database service.
    web service: Defines the Django web service, specifies dependencies, and maps ports.	

Build and Run Docker Containers:
    cmd: $docker-compose build
    Cmd: $docker-compose up
Database Setup
    cmd: $docker-compose exec web python manage.py makemigrations
    cmd: $docker-compose exec web python manage.py migrate
    cmd: $docker-compose exec web python manage.py createsuperuser




Run the Script to Import Data:
    cmd: docker-compose exec web python myapp/scripts.py
	

Endpoints: 
    ProcessProductSpecView:
    About: Defines the API for product specifications and Adding data to Relaxed Regular Fit tables
    Endpoint: /productspecification/

FitListView: 
    About: Defines the fitlist API to filter "relaxed fit" and "regular fit" based on the type of fit.
    Endpoint: /fitlist/
    Method: GET
    Parameters:
    type_of_fit: Specifies the type of fit ('relaxed' or 'regular')





