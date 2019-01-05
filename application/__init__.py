from flask import Flask
import sqlalchemy
from flask_session import Session
from flask_redis import FlaskRedis


# set db
redis_store = FlaskRedis()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():

        # Set global contexts
        redis_store.endpoint = app.config['ENDPOINT']
        redis_store.uri = app.config['SQLALCHEMY_DATABASE_URI']
        redis_store.post_query = app.config['POST_QUERY']
        redis_store.post_like = app.config['QUERY_LIKE']

        # Construct the data set
        from . import routes
        app.register_blueprint(routes.main_blueprint)

        return app
