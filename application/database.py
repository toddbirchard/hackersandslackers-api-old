from sqlalchemy import create_engine, select, text, and_, update
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
import json

class LynxData:
    """Get all fresh Lynx posts, or update them with new HTML."""

    # Set Variables
    def __init__(self, uri, query, query_like):
        self.uri = uri
        self.query = query
        self.query_like = query_like
        self.records = self.fetch_records(self.uri, self.query, self.query_like)

    @classmethod
    def open_connection(self, uri):
        """Open db connection."""
        engine = create_engine(uri, echo=True, strategy='threadlocal', encoding="utf-8", convert_unicode=True)
        Base = declarative_base()
        Base.metadata.create_all(engine)
        return engine

    @classmethod
    def fetch_records(self, uri, query, query_like):
        """Run any query which is passed."""
        engine = self.open_connection(uri)
        META_DATA = MetaData(bind=engine, reflect=True)
        posts = META_DATA.tables['posts']
        rows = []
        # Set up engine
        engine = create_engine(uri, echo=False, strategy='threadlocal', encoding="utf-8", convert_unicode=True)
        META_DATA = MetaData(bind=engine, reflect=True)
        posts = META_DATA.tables['posts']
        Base = declarative_base()
        Base.metadata.create_all(engine)
        # Manage Connection
        with engine.connect() as conn:
            try:
                sql = select([posts.c.slug, posts.c.html]).where( and_(posts.c.title.like('%Lynx%'), posts.c.modified == None)).limit(10)
                results = conn.execution_options(stream_results=True).execute(sql)
                for row in results:
                    rows.append(dict(row))
            except KeyError:
                print('something broke. sorry.')
                raise
            finally:
                conn.close()
                return rows

    @staticmethod
    def update_post(uri, slug, html):
        """Update post with new previews."""
        engine = create_engine(uri, echo=True, strategy='threadlocal', encoding="utf-8", convert_unicode=True)
        Base = declarative_base()
        Base.metadata.create_all(engine)
        META_DATA = MetaData(bind=engine, reflect=True)
        posts = META_DATA.tables['posts']
        with engine.connect() as conn:
            try:
                sql = update(posts).where(posts.c.slug == slug).values(html=html, modified=1)
                results = conn.execution_options(stream_results=True).execute(sql)
                return results
            except KeyError:
                print('something broke. sorry.')
                raise
            finally:
                conn.close()
