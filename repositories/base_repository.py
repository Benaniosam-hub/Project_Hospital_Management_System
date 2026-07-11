from database.connection import get_db_connection, get_db_cursor

class BaseRepository:
    def execute_query(self, query, params=None):
        conn = get_db_connection()
        cursor = get_db_cursor()
        try:
            cursor.execute(query, params)
            conn.commit()
            return cursor
        except Exception as e:
            conn.rollback()
            raise e 
        finally:
            cursor.close()

    def fetch_all(self, query, params=None):
        cursor = get_db_cursor()
        conn = get_db_connection()
        try:
            cursor.execute(query, params)
            conn.commit()
            return cursor.fetchall()
        finally:
            cursor.close()

    def fetch_one(self, query , params=None):
        cursor = get_db_cursor()
        conn = get_db_connection()
        try:
            cursor.execute(query, params)
            conn.commit()
            return cursor.fetchone()
        
        finally:
            cursor.close()