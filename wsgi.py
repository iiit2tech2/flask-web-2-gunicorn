from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Love you Pomu :)"

if __name__ == "__main__":
    application.run()
