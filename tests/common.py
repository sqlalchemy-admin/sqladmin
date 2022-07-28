import os
from typing import Any, List

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine

test_database_uri_sync = os.environ.get(
    "TEST_DATABASE_URI_SYNC",
    "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres",
)
test_database_uri_async = os.environ.get(
    "TEST_DATABASE_URI_ASYNC",
    "postgresql+asyncpg://postgres:postgres@localhost:5432/postgres",
)

sync_engine = create_engine(test_database_uri_sync)
async_engine = create_async_engine(test_database_uri_async)


class DummyData(dict):  # pragma: no cover
    def getlist(self, key: str) -> List[Any]:
        v = self[key]
        if not isinstance(v, (list, tuple)):
            v = [v]
        return v
