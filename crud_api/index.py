from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# app and db config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']


# db stuff
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    email = db.Column(db.String(20))
    phone_number = db.Column(db.Integer)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
