import sqlite3
import pandas as pd

bd_users = pd.read_csv('bank_data.csv')

def create_db():
    conn = sqlite3.connect('bank_data.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS banking_data (
    user_id INTEGER PRIMARY KEY,
    job TEXT,
    marital TEXT,
    education TEXT,
    default_flag TEXT,
    balance REAL,
    housing TEXT,
    loan TEXT,
    contact TEXT,
    day INTEGER,
    month TEXT,
    duration REAL,
    campaign INTEGER,
    pdays INTEGER,
    previous INTEGER,
    poutcome TEXT,
    deposit TEXT
);
''')
    bd_users.to_sql('banking_data',conn,if_exists='replace',index=False)

    conn.commit()
    conn.close()

create_db()