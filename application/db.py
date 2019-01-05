from flask import current_app as app
from SQLAlchemy import create_engine, execute
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base



class LynxData:
    """Query the WeWork Database for Employee & Location information."""

    # Reports row number for response
    rows_queried = 0

    # Set Variables
    def __init__(self):
        self.base_url = app.Config.getConfigValue('BASE_URL')
        self.sqlalchemy_database_uri = app.Config.getConfigValue('SQLALCHEMY_DATABASE_URI')
        self.query = app.Config.getConfigValue('POST_QUERY')
        self.querylike = app.Config.getConfigValue('QUERY_LIKE')

    @classmethod
    def fetch_records(self):
        """Agnostic function which will run whichever query is passed."""
        # Set up engine
        Base = declarative_base()
        engine = create_engine(self.sqlalchemy_database_uri, client_encoding='utf8', echo=True, strategy='threadlocal')
        Base.metadata.create_all(engine)
        # Manage Connection
        with engine.connect() as conn:
            try:
                res = conn.execution_options(stream_results=True).execute(self.query, {':like': self.querylike})  # .construct_params()
                return [dict(row) for row in res]
            except KeyError:
                print('something broke. sorry.')
                raise
            finally:
                conn.close()
