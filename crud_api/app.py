from flask import Flask
import os


def create_app():
    app = Flask(__name__)
    config(app)

    from db.models import db
    db.init_app(app)

    with app.app_context():
        db.create_all()

    from api.api import crud_api
    app.register_blueprint(crud_api)

    return app


def config(app):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']


if __name__ == '__main__':
    create_app().run(debug=True)
