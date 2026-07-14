# Issue & Vulnerability Tracking System

## Project Overview

The Issue & Vulnerability Tracking System is a web-based application developed using Flask and SQLite. The system allows users to create, view, update, delete, search, and sort security issues through a user-friendly dashboard. It provides a simple interface for managing vulnerability records and monitoring their current status.

This project was developed as part of the Dublin Business School assessment to demonstrate the implementation of RESTful APIs, database integration, frontend development, and version control using GitHub.

---

## Features

- Create new security issues
- View all recorded issues
- Update existing issues
- Delete issues
- Search issues by severity
- Sort issues
- Dashboard showing:
  - Total Issues
  - Open Issues
  - In Progress Issues
  - Resolved Issues
- Responsive user interface
- SQLite database integration

---

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML5
- CSS3
- JavaScript
- Git
- GitHub
- Postman

---

## Project Structure

IssueTracker/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── instance/
│   └── issues.db
├── static/
│   ├── style.css
│   └── script.js
├── templates/
│   └── index.html
├── screenshots/
└── references/
    └── resources.md

---

## Installation

### Clone the repository

git clone <repository-url>
cd IssueTracker

### Create a virtual environment

python -m venv venv

### Activate the virtual environment

Windows
venv\Scripts\activate

### Install dependencies

pip install -r requirements.txt

### Run the application

python app.py

Open your browser and visit
http://127.0.0.1:5000

---

## REST API Endpoints

- GET/issues – Retrieve all issues.
- POST/issues – Create a new issue.
- PUT/issues/<id> – Update an existing issue.
- DELETE/issues/<id> – Delete an existing issue.

---

## Database

The application uses SQLite with Flask-SQLAlchemy.

Each issue contains:

- Title
- Description
- Severity
- Status

The database is automatically created when the application is run for the first time.

---

## Testing

The following functionality has been tested:

- Create Issue
- View Issues
- Update Issue
- Delete Issue
- Search by Severity
- Sort Issues
- Dashboard statistics
- REST API testing using Postman

---

## GitHub Development

The project was developed using Git and GitHub with progressive commits throughout development.

The repository includes:

- Source code
- Project documentation
- Screenshots
- References
- Version history

---

## Code Attribution Summary

The project was primarily developed by me. External resources were used for learning and reference during development.

* Self:Project implementation, feature integration, testing, Git management, documentation, search, sorting, validation, dashboard, and reporting features.
* Flask Documentation:Flask application setup, routing, and project structure.https://python-adv-web-apps.readthedocs.io/en/latest/flask.html
* Flask CRUD API Tutorial (YouTube):Guidance on REST API concepts and CRUD implementation.https://youtu.be/oQ5UfJqW5Jo
* GitHub Documentation:README structure and Markdown formatting.
* OpenAI ChatGPT for frontend :Assistance with HTML, CSS, JavaScript, debugging, and code explanations.

A complete list of references, learning resources, AI assistance, and development tools is available in `resources.md`.


---

## Future Enhancements

Possible future improvements include:

- User authentication
- Role-based access control
- Issue assignment
- Email notifications
- Advanced filtering
- Charts and analytics dashboard
- Export issues to PDF or CSV

---

👤 Contributor

Vandana Ramanjinappa

