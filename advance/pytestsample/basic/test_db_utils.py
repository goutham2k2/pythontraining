# test_db_utils.py

import sqlite3
import pytest
from db_utils import init_db, add_user, get_users

@pytest.fixture
def db_connection():
    conn = sqlite3.connect(":memory:")  # In-memory DB
    init_db(conn)
    yield conn
    conn.close()

def test_add_and_get_user(db_connection):
    add_user(db_connection, "Alice")
    users = get_users(db_connection)
    assert len(users) == 1
    assert users[0][1] == "Alice"
