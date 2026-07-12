# Issue & Vulnerability Tracking System

## Project Overview

The **Issue & Vulnerability Tracking System** is a web-based application developed using **Flask** and **SQLite**. The system allows users to create, view, update, delete, search, and sort security issues through a user-friendly dashboard. It provides a simple interface for managing vulnerability records and monitoring their current status.

This project was developed as part of the **Dublin Business School** assessment to demonstrate the implementation of RESTful APIs, database integration, frontend development, and version control using GitHub.

---

## Features

* Create new security issues
* View all recorded issues
* Update existing issues
* Delete issues
* Search issues by severity
* Sort issues
* Dashboard showing:

  * Total Issues
  * Open Issues
  * In Progress Issues
  * Resolved Issues
* Responsive user interface
* SQLite database integration

---

## Technologies Used

* Python 3
* Flask
* Flask-SQLAlchemy
* SQLite
* HTML5
* CSS3
* JavaScript
* Git & GitHub

---

## Project Structure

```text
Issuetracker/
│
├── app.py
├── README.md
├── .gitignore
├── static/
│   ├── style.css
│   └── script.js
├── templates/
│   └── index.html
├── instance/          (Automatically generated SQLite database)
└── venv/              (Virtual environment - excluded from Git)
```

---

## Installation

### Clone the repository

```bash
git clone <repository-url>
cd Issuetracker
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install Flask Flask-SQLAlchemy
```

### Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## REST API Endpoints

| Method | Endpoint     | Description              |
| ------ | ------------ | ------------------------ |
| GET    | /issues      | Retrieve all issues      |
| POST   | /issues      | Create a new issue       |
| PUT    | /issues/<id> | Update an existing issue |
| DELETE | /issues/<id> | Delete an issue          |

---

## Database

The application uses **SQLite** with **Flask-SQLAlchemy**.

Each issue record contains:

* ID
* Title
* Description
* Severity
* Status

The database is automatically created when the application runs for the first time.

---

## Testing

The following functionality has been tested:

* Create Issue
* View Issues
* Update Issue
* Delete Issue
* Search by Severity
* Sort Issues
* Dashboard statistics update automatically

---

## GitHub Development

The project was developed using Git and GitHub with progressive commits to demonstrate the development process. Code attribution has been included in commit messages where external learning resources were used.

---

## Code Attribution

The following resources were used during the development of this project:

### Flask Documentation

https://flask.palletsprojects.com/

Used for:

* Flask application structure
* Routing
* Request handling
* JSON responses

### Flask-SQLAlchemy Documentation

https://flask-sqlalchemy.palletsprojects.com/

Used for:

* Database configuration
* Model creation
* CRUD operations

### Flask Tutorial

https://python-adv-web-apps.readthedocs.io/en/latest/flask.html

Used for understanding Flask application development.

### AI Assistance (ChatGPT)

OpenAI ChatGPT was used to assist with:

* Frontend HTML layout
* CSS styling
* JavaScript implementation
* Dashboard design
* Search and sorting functionality
* General code explanation and debugging

All generated code was reviewed, modified, tested, and integrated by the project author.

---

## Future Enhancements

Possible future improvements include:

* User authentication
* Role-based access control
* Issue assignment
* Email notifications
* Advanced filtering
* Charts and analytics dashboard
* Export issues to PDF or CSV

---

## Author

**Vandana Ramanjinappa**

Dublin Business School

Module Assessment – Issue & Vulnerability Tracking System
