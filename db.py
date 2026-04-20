import aiosqlite

DB_NAME = "vpn.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            vpn_key TEXT,
            days_left INTEGER DEFAULT 0,
            balance REAL DEFAULT 0
        )
        """)
        await db.commit()


async def get_user(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            "SELECT * FROM users WHERE user_id=?",
            (user_id,)
        )
        return await cursor.fetchone()


async def add_user(user_id, username):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)",
            (user_id, username)
        )
        await db.commit()


async def update_subscription(user_id, days, key):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "UPDATE users SET days_left=?, vpn_key=? WHERE user_id=?",
            (days, key, user_id)
        )
        await db.commit()


async def decrease_days():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "UPDATE users SET days_left = days_left - 1 WHERE days_left > 0"
        )
        await db.commit()