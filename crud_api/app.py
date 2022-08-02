from flask import Flask
import os


def create_app() -> Flask:
    app = Flask(__name__)
    config(app)

    from crud_api.db.models import db
    db.init_app(app)
    db.create_all(app=app)

    from crud_api.api.api import crud_api
    app.register_blueprint(crud_api)

    return app


def config(app):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']


if __name__ == '__main__':
    create_app().run(debug=True)
