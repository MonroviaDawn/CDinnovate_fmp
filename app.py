from flask import Flask, Blueprint, request
from views import views
#we import our views from the views file

app = Flask(__name__)
#we instantiate the app object

app.register_blueprint(views)
#we register the views Blueprint

if __name__ == "__main__":
    app.run(debug=True, port=8000)
#running the application

