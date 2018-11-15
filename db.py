from sqlalchemy import create_engine, text


class get_lynx_posts:
    """Selects records for all confirmed new hires which have yet to be onboarded."""

    def __init__(self, config):
        self.uri = config.uri
        self.query = config.query
        self.rows = self.get_posts()
        self.count = self.rows.rowcount

    def get_posts(self):
        engine = create_engine(self.uri, client_encoding='utf8', echo=True)
        with engine.connect() as conn:
            sql = text(self.query)
            results = conn.execute(sql)
            conn.close()
            return results
