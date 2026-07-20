import os
import asyncpg
from contextlib import asynccontextmanager
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME', 'hms_db')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')


class AsyncDatabase:
    def __init__(self):
        self.pool = None

    async def connect(self):

        self.pool = await asyncpg.create_pool(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT,
            min_size=10,  
            max_size=50
        )
        print("Database connection successful.")

    async def disconnect(self):
        if self.pool:
            await self.pool.close()
            print("Database connection pool closed.")

    @asynccontextmanager
    async def get_connection(self):
        if not self.pool:
            raise RuntimeError("Database pool has not been initialized. Call connect() first.")
        
        async with self.pool.acquire() as connection:
            yield connection

db = AsyncDatabase()