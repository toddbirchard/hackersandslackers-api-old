from sqlalchemy import *
import pandas as pd

class get_lynx_posts:
    """Selects records for all confirmed new hires which have yet to be onboarded."""

    def __init__(self, config):
        """Set DB config values."""
        self.uri = config.uri
        self.query = str.format(config.query)
        self.query_like = config.query_like
        self.rows = self.get_posts()

    def get_posts(self):
        """Retrieve all rows."""
        engine = create_engine(self.uri, echo=True)
        q = text(self.query)
        lynx_df = pd.read_sql(q, engine, params={'x': self.query_like})
        print(lynx_df.head(10))
        return lynx_df
