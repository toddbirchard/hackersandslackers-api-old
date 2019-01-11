from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class LynxData:
    """Query the WeWork Database for Employee & Location information."""

    # Set Variables
    def __init__(self, uri, query, query_like):
        self.uri = uri
        self.query = query
        self.query_like = query_like
        self.records = self.fetch_records(self.uri, self.query, self.query_like)

    @classmethod
    def fetch_records(self, uri, query, query_like):
        """Run any query which is passed."""
        rows = []
        # Set up engine
        engine = create_engine(uri, echo=True)
        Base = declarative_base()
        Base.metadata.create_all(engine)
        # Manage Connection
        with engine.connect() as conn:
            try:
                results = conn.execution_options(stream_results=True).execute(query)  # .construct_params()
                for row in results:
                    rows.append(dict(row))
                    print(dict(row))
                return rows
            except KeyError:
                print('something broke. sorry.')
                raise
            finally:
                conn.close()
