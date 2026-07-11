import psycopg2
from psycopg2.extras import RealDictCursor
from flask import current_app, g

def get_db_connection():
    if 'db_conn' not in g:
        g.db_conn = psycopg2.connect(
            host=current_app.config['DB_HOST'],
            database=current_app.config['DB_NAME'],
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASSWORD'],
            port=current_app.config['DB_PORT']
        )
    return g.db_conn

def get_db_cursor():
    conn=get_db_connection()
    return conn.cursor(cursor_factory=RealDictCursor)

def close_db_connection(e=None):
    conn = g.pop('db_conn', None)
    if conn is not None:
        conn.close()