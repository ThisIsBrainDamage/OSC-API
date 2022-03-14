import asyncpg

from main import DATABASE_URL


async def main():
    async with await asyncpg.connect(DATABASE_URL) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS Users (
            name TEXT
        )""")