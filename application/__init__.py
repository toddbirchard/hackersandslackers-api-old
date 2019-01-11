from flask import Flask
import sqlalchemy
from flask_sqlalchemy import Model, SQLAlchemy
from flask_session import Session
from flask_redis import FlaskRedis

r = FlaskRedis()
db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        # Set Global Session Variables
        r.init_app(app, charset="utf-8", decode_responses=True)
        r.set('endpoint', app.config['ENDPOINT'])
        r.set('uri', app.config['SQLALCHEMY_DATABASE_URI'])
        r.set('query', app.config['POST_QUERY'])
        r.set('query_like', app.config['QUERY_LIKE'])

        # Initialize Global db
        db.init_app(app)

        # HTML structure for new Lynx posts
        from . import  preview

        # Construct the data set
        from . import routes
        app.register_blueprint(routes.main_blueprint)

        return app
