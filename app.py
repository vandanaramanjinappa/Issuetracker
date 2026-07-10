from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///issues.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Code Attribution:
# Flask framework reference:
# https://python-adv-web-apps.readthedocs.io/en/latest/flask.html
#
# Flask tutorial reference:
# https://youtu.be/oQ5UfJqW5Jo?si=c8DqVvnp8oKWG-2z
#
# Flask-SQLAlchemy reference:
# https://flask-sqlalchemy.palletsprojects.com/


# Issue database model
class Issue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    severity = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)


@app.route('/')
def home():
    return "Issue and Vulnerability Tracking System is running!"

@app.route("/dashboard")
def dashboard():
    return render_template("index.html")


# READ - Get all issues with search by severity
@app.route("/issues", methods=["GET"])
def get_issues():

    severity = request.args.get("severity")
    sort = request.args.get("sort")

    if severity:
        query = Issue.query.filter_by(severity=severity)
    else:
        query = Issue.query

    if sort == "desc":
        all_issues = query.order_by(Issue.id.desc()).all()
    else:
        all_issues = query.order_by(Issue.id.asc()).all()

    result = []

    for issue in all_issues:
        result.append({
            "id": issue.id,
            "title": issue.title,
            "description": issue.description,
            "severity": issue.severity,
            "status": issue.status
        })

    return jsonify(result)

# CREATE - Add new issue with validation
@app.route("/issues", methods=["POST"])
def create_issue():

    data = request.json

    if not data.get("title"):
        return jsonify({"message": "Title is required"}), 400

    if not data.get("description"):
        return jsonify({"message": "Description is required"}), 400

    valid_severity = ["Low", "Medium", "High", "Critical"]

    if data.get("severity") not in valid_severity:
        return jsonify({"message": "Invalid severity value"}), 400

    valid_status = ["Open", "In Progress", "Resolved"]

    if data.get("status") not in valid_status:
        return jsonify({"message": "Invalid status value"}), 400

    new_issue = Issue(
        title=data["title"],
        description=data["description"],
        severity=data["severity"],
        status=data["status"]
    )

    db.session.add(new_issue)
    db.session.commit()

    return jsonify({
        "message": "Issue created successfully",
        "issue": {
            "id": new_issue.id,
            "title": new_issue.title,
            "description": new_issue.description,
            "severity": new_issue.severity,
            "status": new_issue.status
        }
    }), 201


# UPDATE - Update existing issue
@app.route("/issues/<int:id>", methods=["PUT"])
def update_issue(id):

    issue = Issue.query.get(id)

    if issue:

        data = request.json

        issue.title = data.get("title", issue.title)
        issue.description = data.get("description", issue.description)
        issue.severity = data.get("severity", issue.severity)
        issue.status = data.get("status", issue.status)

        db.session.commit()

        return jsonify({
            "message": "Issue updated successfully"
        })

    return jsonify({
        "message": "Issue not found"
    }), 404

# DELETE - Remove issue
@app.route("/issues/<int:id>", methods=["DELETE"])
def delete_issue(id):

    issue = Issue.query.get(id)

    if issue:

        db.session.delete(issue)
        db.session.commit()

        return jsonify({
            "message": "Issue deleted successfully"
        })

    return jsonify({
        "message": "Issue not found"
    }), 404

# REPORT - Issue summary
@app.route("/report", methods=["GET"])
def report():

    total = Issue.query.count()
    open_count = Issue.query.filter_by(status="Open").count()
    resolved_count = Issue.query.filter_by(status="Resolved").count()
    in_progress_count = Issue.query.filter_by(status="In Progress").count()

    return jsonify({
        "total_issues": total,
        "open_issues": open_count,
        "resolved_issues": resolved_count,
        "in_progress_issues": in_progress_count
    })


# Create database table
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)