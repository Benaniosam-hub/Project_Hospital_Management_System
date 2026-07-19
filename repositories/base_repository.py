from database.connection import db

class BaseRepository:
    def _format_query(self, query: str) -> str:
        """
        Helper to convert Flask/psycopg2 %s placeholders to asyncpg $1, $2 syntax.
        If your queries are already written using $1, $2, this wont break them.
        """
        if "%s" in query:
            parts = query.split("%s")
            new_query = ""
            for i, part in enumerate(parts[:-1]):
                new_query += f"{part}${i+1}"
            new_query += parts[-1]
            return new_query
        return query
    
    async def execute_query(self, query: str, params: tuple = None):
        formatted_query = self._format_query(query)
        params = params or ()

        async with db.get_connection() as conn:
            return await conn.execute(formatted_query, *params)

    async def fetch_all(self, query: str, params: tuple = None) -> list:
        formatted_query = self._format_query(query)
        params = params or ()

        async with db.get_connection() as conn:
            records = await conn.fetchrow(formatted_query, *params)
            return [dict(record) for record in records]

    async def fetch_one(self, query: str, params: tuple = None) -> dict:
        formatted_query = self._format_query(query)
        params = params or ()

        async with db.get_connection() as conn:
            record = await conn.fetchrow(formatted_query, *params)
            return dict(record) if record else None
        