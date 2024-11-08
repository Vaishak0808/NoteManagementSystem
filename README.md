###### NoteManagementSystem
# Note Management System
This repository contains a Django-based notes Management System with JWT authentication. The application provides features for user authentication (sign up, login, logout), and CRUD operations for notes.

### Features
- User Authentication (Sign Up, Login, Logout)
- JWT Authentication for secure access
- Create, Read, Update, and Delete (CRUD) operations for notes
- Pagination for listing notes
- Detailed logging of errors

### Installation
Clone the repository:
```
git clone https://github.com/Vaishak0808/NoteManagementSystem.git
```
Navigate to the project directory:
```
cd NoteManagementSystem
```
Install the required packages:
```
pip install -r requirements.txt
```
Run the development server:
```
python manage.py runserver
```
### Dockerization
To run the application using Docker, follow these steps:

Build the Docker image:
```
docker build -t notes_app .
```
Run the Docker container:
```
docker run -p 8000:8000 notes_app
```
### Logging
Errors are logged to log/error.log. This can be configured in the ins_logger module.

### Pagination
The Paginator module in django.core handles pagination for the notes list and sets the page size to 10.
