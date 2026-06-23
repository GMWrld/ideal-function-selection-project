from database.db_manager import DatabaseManager


def test_database_connection():

    db = DatabaseManager()

    session = db.get_session()

    assert session is not None