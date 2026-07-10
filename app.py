from flask import Flask, jsonify, request

app = Flask(__name__)

# Code Attribution:
# Flask framework reference:
# https://python-adv-web-apps.readthedocs.io/en/latest/flask.html
#
# Flask tutorial reference:
# https://youtu.be/oQ5UfJqW5Jo?si=c8DqVvnp8oKWG-2z


issues = [
    {
        "id": 1,
        "title": "Login authentication failure",
        "description": "Users cannot login to the system",
        "severity": "High",
        "status": "Open"
    },
    {
        "id": 2,
        "title": "Outdated security dependency",
        "description": "A dependency requires a security update",
        "severity": "Medium",
        "status": "Resolved"
    }
]


@app.route('/')
def home():
    return "Issue and Vulnerability Tracking System is running!"


@app.route("/issues", methods=["GET"])
def get_issues():
    return jsonify(issues)


@app.route("/issues", methods=["POST"])
def create_issue():

    new_issue = request.json

    issues.append(new_issue)

    return jsonify({
        "message": "Issue created successfully",
        "issue": new_issue
    }), 201

@app.route("/issues/<int:id>", methods=["PUT"])
def update_issue(id):

    for issue in issues:
        if issue["id"] == id:

            updated_data = request.json

            issue.update(updated_data)

            return jsonify({
                "message": "Issue updated successfully",
                "issue": issue
            })

    return jsonify({
        "message": "Issue not found"
    }), 404


if __name__ == '__main__':
    app.run(debug=True)
