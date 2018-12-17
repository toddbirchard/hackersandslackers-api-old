import os
from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config_loader.BaseConfig')

    with app.app_context():

        # Set up database to be used globally
        db = SQLAlchemy(app)

        # Make endpoint global
        g.endpoint = app.config.gcloud_endpoint

        # Construct the data set
        from . import routes
        app.register_blueprint(routes.preview_blueprint)

        return app
