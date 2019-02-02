from sqlalchemy import create_engine, select, text, and_, update
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from . import r


class LynxData:
    """Get all fresh Lynx posts, or update them with new HTML."""

    session = None

    __uri = r.get('uri')
    __query = r.get('query')
    __query_like = r.get('query_like')
    __engine = create_engine(__uri, echo=True, strategy='threadlocal', encoding="utf-8", convert_unicode=True)

    @classmethod
    def open_session(cls):
        """Open db connection."""
        Base = declarative_base()
        Base.metadata.create_all(cls.__engine)
        Session = sessionmaker(bind=cls.__engine)
        session = Session()
        cls.session = session
        return session

    @classmethod
    def fetch_records(cls):
        """Run any query which is passed."""
        engine = cls.open_session()
        META_DATA = MetaData(bind=engine, reflect=True)
        posts = META_DATA.tables['posts']
        rows = []
        # Set up engine
        # engine = create_engine(uri, echo=False, strategy='threadlocal', encoding="utf-8", convert_unicode=True)
        # Manage Connection
        with engine.connect() as conn:
            try:
                sql = select([posts.c.slug, posts.c.html]).where(and_(posts.c.title.like('%Lynx%'), posts.c.modified is None)).limit(30)
                results = conn.execution_options(stream_results=True).execute(sql)
                for row in results:
                    rows.append(dict(row))
            except KeyError:
                print('something broke. sorry.')
                raise
            finally:
                conn.close()
            return rows

    @classmethod
    def update_post(cls, slug, html):
        """Update post with new previews."""
        Base = declarative_base()
        Base.metadata.create_all(cls.open_session())
        META_DATA = MetaData(bind=cls.open_session(), reflect=True)
        posts = META_DATA.tables['posts']
        with cls.open_session() as conn:
            try:
                sql = update(posts).where(posts.c.slug == slug).values(html=html, modified=1)
                results = conn.execution_options(stream_results=True).execute(sql)
                return results
            except KeyError:
                print('something broke. sorry.')
                raise
            finally:
                conn.close()
