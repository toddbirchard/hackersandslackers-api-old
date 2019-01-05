from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class LynxData:
    """Query the WeWork Database for Employee & Location information."""

    # Set Variables
    def __init__(self, uri, query, querylike):
        self.uri = uri
        self.query = query
        self.querylike = querylike
        self.records = self.fetch_records(self.uri, self.query, self.querylike)

    @classmethod
    def fetch_records(self, uri, query, querylike):
        """Agnostic function which will run whichever query is passed."""
        # Set up engine
        rows = []
        Base = declarative_base()
        engine = create_engine(uri, echo=True, strategy='threadlocal')
        Base.metadata.create_all(engine)
        # Manage Connection
        with engine.connect() as conn:
            try:
                res = conn.execution_options(stream_results=True).execute(query)  # .construct_params()
                for row in res:
                    rows.append(dict(row))
                    print(dict(row))
                return rows
            except KeyError:
                print('something broke. sorry.')
                raise
            finally:
                conn.close()
