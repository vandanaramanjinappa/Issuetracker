from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Issue and Vulnerability Tracking System is running!"

if __name__ == '__main__':
    app.run(debug=True)