# Apk Manager

## Overview

Apk Manager is a Django-based application designed to manage APK files. The platform allows users to upload, update, delete, and view their APK files, supporting multilingual functionality. It utilizes Docker for containerization, making deployment and management easier.

## Features

- **User Authentication**: Register, login, and manage user accounts.
- **App Management**: List, add, update, and delete uploaded APK files.
- **Multilingual Support**: Switch between English and French languages.
- **Docker Integration**: Containerized deployment using Docker.

## Requirements

- Docker
- Docker Compose
- Python 3.10 or later
- MySQL 8.0 or later

## Installation

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/apk-manager.git
cd apk-manager
```

## Set Up Docker

Ensure Docker and Docker Compose are installed and running on your machine. Follow these steps to set up Docker:

### Build and Run the Application

```bash
docker-compose up --build -d
```

#### This command will:

- Build the Docker containers.
- Run database migrations.
- Start the Django server.

## Create a Superuser
After the containers are up and running, create a superuser to manage the application:

``` bash
docker-compose exec web python manage.py createsuperuser
```

## Access the Application
Once Docker is set up and running, you can access the application via:

Web Application: http://localhost:8000

## Usage
### User Registration and Login
- Register: Visit /register/ to create a new user account.
- Login: Visit /login/ to access your account.


### App Management
- Add App: Navigate to /add_app/ to upload a new APK file.
- Update App: Edit existing apps via /update_app/<app_id>/.
- Delete App: Remove apps through /delete_app/<app_id>/.
- View Apps: List all your apps at /app_list/.

### Multilingual Support
To switch between English and French:
Click on the language selector in the top right corner of the application interface.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
