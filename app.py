from flask import Flask, jsonify

app = Flask(__name__)
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


@app.route("/issues", methods=["GET"])
def get_issues():
    return jsonify(issues)


if __name__ == '__main__':
    app.run(debug=True)
@app.route('/')
def home():
    return "Issue and Vulnerability Tracking System is running!"

if __name__ == '__main__':
    app.run(debug=True)
    # Code Attribution:
# Flask framework reference:
# https://python-adv-web-apps.readthedocs.io/en/latest/flask.html
#
# Flask tutorial reference:
# https://youtu.be/oQ5UfJqW5Jo?si=c8DqVvnp8oKWG-2z

