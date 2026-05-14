import sqlite3
import pandas as pd
from sql.database import get_connection


def _run(query: str, params: tuple = ()) -> pd.DataFrame:
    conn = get_connection()
    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    return df


def shared_years():
    """Years present in all four datasets (INNER JOIN)."""
    return _run("""
        SELECT p.year,
               p.value AS population,
               r.value AS remuneration,
               i.value AS ict_companies,
               b.value AS bike_lanes
        FROM population p
        JOIN remuneration r ON r.year = p.year
        JOIN ict_companies i ON i.year = p.year
        JOIN bike_lanes b ON b.year = p.year
        ORDER BY p.year
    """)


def years_above_remuneration(threshold: float):
    """Years where average remuneration exceeds the given threshold (WHERE)."""
    return _run("""
        SELECT year, value AS remuneration
        FROM remuneration
        WHERE value > ?
        ORDER BY year
    """, (threshold,))


def decade_averages():
    """Average value per decade for each indicator (GROUP BY)."""
    return _run("""
        SELECT (p.year / 10) * 10 AS decade,
               AVG(p.value) AS avg_population,
               AVG(r.value) AS avg_remuneration,
               AVG(i.value) AS avg_ict_companies,
               AVG(b.value) AS avg_bike_lanes
        FROM population p
        JOIN remuneration r ON r.year = p.year
        JOIN ict_companies i ON i.year = p.year
        JOIN bike_lanes b ON b.year = p.year
        GROUP BY decade
        ORDER BY decade
    """)


def decades_with_ict_growth(min_avg: float):
    """Decades where average ICT companies count exceeds threshold (HAVING)."""
    return _run("""
        SELECT (year / 10) * 10 AS decade,
               AVG(value) AS avg_ict
        FROM ict_companies
        GROUP BY decade
        HAVING AVG(value) > ?
        ORDER BY decade
    """, (min_avg,))


def population_years_missing_in_ict():
    """Years in population data that have no matching record in ict_companies (NOT IN)."""
    return _run("""
        SELECT year
        FROM population
        WHERE year NOT IN (SELECT year FROM ict_companies)
        ORDER BY year
    """)