import os
import sqlite3
import uuid
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Always create finance.db in project root, regardless of where script is run from
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "../../finance.db")  # go up 2 levels

def random_account_name(state):
    return state[0] + ''.join([str(random.randint(0, 9)) for _ in range(5)])

def run_sql_file(cursor, filename):
    with open(filename, "r") as f:
        cursor.executescript(f.read())

def seed():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print(f"🌱 Seeding database at: {os.path.abspath(DB_PATH)}")

    # 1. Run schema
    run_sql_file(cursor, os.path.join(BASE_DIR, "setup.sql"))

    # 2. Insert accounts
    states = ['California', 'Texas', 'Florida', 'New York', 'Illinois',
              'Georgia', 'Ohio', 'Arizona', 'Michigan', 'North Carolina']
    account_names = []

    for state in states:
        name = random_account_name(state)
        account_names.append(name)
        cursor.execute(
            "INSERT INTO accounts (account_name, accounting_region) VALUES (?, ?)",
            (name, state)
        )

    # 3. Insert transactions
    for _ in range(200):
        account = random.choice(account_names)
        trade_date = fake.date_between(start_date='-30d', end_date='today')
        settlement_date = trade_date + timedelta(days=2)
        amount = round(random.uniform(1000, 100000), 2)
        cursor.execute(
            "INSERT INTO transactions (transaction_id, account_name, amount, trade_date, settlement_date) "
            "VALUES (?, ?, ?, ?, ?)",
            (str(uuid.uuid4()), account, amount, trade_date, settlement_date)
        )

    conn.commit()
    conn.close()
    print("✅ Database seeded successfully.")

if __name__ == "__main__":
    seed()
