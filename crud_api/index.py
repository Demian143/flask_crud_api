from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# app and db config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
db = SQLAlchemy(app)

# example of how to make models


class User(db.model):
    pass

# api endpoints example


@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api():
    if request.methd == 'GET':
        pass
    if request.method == 'POST':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass


if __name__ == '__main__':
    app.run(debug=True)
