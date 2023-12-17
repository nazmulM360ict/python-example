from flask import Flask

application = Flask(__name__)

@application.route("/")
def home_route():
    return "This is home route"

if __name__ == '__main__':
    application.run()
