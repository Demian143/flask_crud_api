from flask import Flask
from flask_migrate import Migrate
import os


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']

    # it's no need to db.create_all(), it does by itself
    from db.models import db
    db.init_app(app)

    with app.app_context():
        db.create_all()

    migrate = Migrate(app, db)
    migrate.init_app(app, db)

    from api.api import crud_api
    app.register_blueprint(crud_api)

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
