import sqlite3
import os
import pandas as pd

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'output', 'torino_data.db')


def get_connection():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    return sqlite3.connect(DB_PATH)


def _load_series(cursor, table_name, series: pd.Series):
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            year  INTEGER PRIMARY KEY,
            value REAL
        )
    """)
    cursor.execute(f"DELETE FROM {table_name}")
    cursor.executemany(
        f"INSERT INTO {table_name} (year, value) VALUES (?, ?)",
        [(int(year), float(val)) for year, val in series.items() if pd.notna(val)]
    )


def build_database(population, remuneration, ict_companies, bike_lanes):
    conn = get_connection()
    cur = conn.cursor()

    _load_series(cur, 'population', population)
    _load_series(cur, 'remuneration', remuneration)
    _load_series(cur, 'ict_companies', ict_companies)
    _load_series(cur, 'bike_lanes', bike_lanes)

    conn.commit()
    conn.close()
    print(f"Database built at: {DB_PATH}")