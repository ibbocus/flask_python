from flask import Flask

# import flask

# In order for us to use flask, we need to create an instance of our app

app = Flask(__name__)


# Syntax to create flask instance


# Syntax for decorators to create a web route
@app.route("/")
def index():
    return "Welcome to MVC with flask project"

@app.route("/<user>")
def welcome_user(user):
    return f"Welcome {user}"



# exercise:- create a function called welcome_user
# create a decorator to link the page /user
# return "welcome to Python flask app dear {user}
# in the browser when we load the page from home page to user name i.e your name
# it should display your name in the browser with message from your methods


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)

