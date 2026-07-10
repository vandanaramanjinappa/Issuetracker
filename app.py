from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

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


# Create database table
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)