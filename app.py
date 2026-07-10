from flask import Flask

app = Flask(__name__)

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