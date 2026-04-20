import sqlite3
from datetime import datetime, timedelta

conn = sqlite3.connect("vpn.db", check_same_thread=False)
cursor = conn.cursor()

# ================= СОЗДАНИЕ ТАБЛИЦЫ =================
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    end_date TEXT,
    vpn_key TEXT
)
""")
conn.commit()


# ================= ДОБАВИТЬ ПОЛЬЗОВАТЕЛЯ =================
def add_user(user_id, username=""):
    cursor.execute("""
        INSERT OR IGNORE INTO users (user_id, username)
        VALUES (?, ?)
    """, (user_id, username))
    conn.commit()


# ================= ОБНОВИТЬ ПОДПИСКУ =================
def update_subscription(user_id, days, key):
    end = datetime.now() + timedelta(days=days)

    cursor.execute("""
        UPDATE users
        SET end_date=?, vpn_key=?
        WHERE user_id=?
    """, (end.isoformat(), key, user_id))

    conn.commit()


# ================= ПОЛУЧИТЬ ПОЛЬЗОВАТЕЛЯ =================
def get_user(user_id):
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    return cursor.fetchone()


# ================= ДНЕЙ ОСТАЛОСЬ =================
def get_days_left(user_id):
    user = get_user(user_id)

    if not user:
        return 0

    end_date = user[2]

    if not end_date:
        return 0

    end = datetime.fromisoformat(end_date)
    return max((end - datetime.now()).days, 0)