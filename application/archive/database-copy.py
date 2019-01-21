from sqlalchemy import create_engine, select, text, and_, sessionmaker
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
import json

class LynxData:
    """Query the WeWork Database for Employee & Location information."""

    # Set Variables
    def __init__(self, uri, query, query_like):
        self.uri = uri
        self.query = query
        self.query_like = query_like
        self.records = self.fetch_records(self.uri, self.query, self.query_like)
        self.engine = self.make_engine(self.uri)
        self.session = self.make_session(self.engine)
        self.posts = self.make_metadata(self.engine)


    def make_engine(self, uri):
        engine = create_engine(uri, echo=True, strategy='threadlocal', encoding="utf-8", convert_unicode=True)
        Base = declarative_base()
        Base.metadata.create_all(engine)
        return engine

    def make_session(self, engine):
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

    def make_metadata(self, engine):
        META_DATA = MetaData(bind=engine, reflect=True)
        posts = META_DATA.tables['posts']
        return posts

    @classmethod
    def fetch_records(self, uri, query, query_like):
        """Run any query which is passed."""
        rows = []
        # Manage Connection
        with self.engine.connect() as conn:
            try:
                sql = select([self.posts.c.slug, self.posts.c.html]).limit(10).where( and_(self.posts.c.title.like('%Lynx%'), self.posts.c.modified == None)).limit(10)
                results = conn.execution_options(stream_results=True).execute(sql)
                for row in results:
                    rows.append(row.__dict__)
                return rows
            except KeyError:
                print('something broke. sorry.')
                raise
            finally:
                conn.close()
