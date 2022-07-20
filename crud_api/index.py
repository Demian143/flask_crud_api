from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# app and db config
app = Flask(__name__)
app.config['SQLALCHMY_DATABASE_URI'] = os.environ['SQLALCHMY_DATABASE_URI']
db = SQLAlchemy(app)

# example of how to make models
class User(db.model):
    pass

# api endpoints example
@app.route('/', methods=['GET', 'POST','PUT','DELETE'])
def api():
    if request.methd == 'GET':
        pass
    if request.method == 'POST':
        pass
    if request.methd == 'PUT':
        pass
    if request.methd == 'DELETE':
        pass

if __name__ == '__main__':
    app.run(debug=True)