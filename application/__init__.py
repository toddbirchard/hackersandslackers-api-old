from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# set db
db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    migrate = Migrate(app, db)

    with app.app_context():
        db.init_app(app)

        # Set global contexts
        g.endpoint = app.config['ENDPOINT']
        g.uri = app.config['SQLALCHEMY_DATABASE_URI']

        # Construct the data set
        from . import routes
        from. import models

        return app
