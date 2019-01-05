from flask import Flask
import sqlalchemy
from flask_session import Session
from flask_redis import FlaskRedis
from redis import StrictRedis

redis_store = FlaskRedis()

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    # redis_store = FlaskRedis(app, strict=False)



    with app.app_context():
        redis_store.init_app(app)
        # Set global contexts
        endpoint = app.config['ENDPOINT']

        redis_store.set('endpoint', endpoint)
        redis_store.set('uri', str(app.config['SQLALCHEMY_DATABASE_URI']).encode('utf-8'))
        redis_store.set('query', str(app.config['POST_QUERY']).encode('utf-8'))
        redis_store.set('querylike', str(app.config['QUERY_LIKE']).encode('utf-8'))



        # Construct the data set
        from . import routes
        app.register_blueprint(routes.main_blueprint)

        return app
