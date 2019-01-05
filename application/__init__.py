from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_redis import FlaskRedis


# set db
db = SQLAlchemy()
redis_store = FlaskRedis()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        db.init_app(app)

        # Set global contexts
        redis_store.endpoint = app.config['ENDPOINT']
        redis_store.uri = app.config['SQLALCHEMY_DATABASE_URI']
        redis_store.post_query = app.config['POST_QUERY']
        redis_store.post_like = app.config['QUERY_LIKE']
        db = SQLAlchemy(app)

        # Construct the data set
        from . import routes

        return app
