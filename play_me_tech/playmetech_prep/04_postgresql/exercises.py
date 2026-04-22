"""
═══════════════════════════════════════════════════════════════════
 TOPIC 4: PostgreSQL — Queries, Deduplication & Data Modelling
═══════════════════════════════════════════════════════════════════

WHY THIS MATTERS FOR PLAYMETECH:
  Sports data pipelines store millions of records. You need to be
  comfortable writing SQL to query, clean, and model that data.
  PostgreSQL is the go-to for this kind of work.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 THEORY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CORE SQL YOU MUST KNOW:
  SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT
  JOIN (INNER, LEFT, RIGHT, FULL OUTER)
  Aggregate functions: COUNT, SUM, AVG, MIN, MAX
  Window functions:    ROW_NUMBER(), RANK(), LAG(), LEAD()
  Subqueries and CTEs (WITH ...)
  INSERT, UPDATE, DELETE, UPSERT (INSERT ... ON CONFLICT)

DEDUPLICATION PATTERNS:
  -- Find duplicates
  SELECT home_team, away_team, match_date, COUNT(*)
  FROM matches
  GROUP BY home_team, away_team, match_date
  HAVING COUNT(*) > 1;

  -- Delete duplicates, keep lowest id
  DELETE FROM matches
  WHERE id NOT IN (
      SELECT MIN(id)
      FROM matches
      GROUP BY home_team, away_team, match_date
  );

  -- Using ROW_NUMBER() (more flexible)
  WITH ranked AS (
      SELECT *, ROW_NUMBER() OVER (
          PARTITION BY home_team, away_team, match_date
          ORDER BY created_at DESC   -- keep newest
      ) AS rn
      FROM matches
  )
  DELETE FROM matches WHERE id IN (
      SELECT id FROM ranked WHERE rn > 1
  );

UPSERT (idempotent inserts):
  INSERT INTO matches (home_team, away_team, match_date, score)
  VALUES ('Arsenal', 'Chelsea', '2024-03-15', '2-1')
  ON CONFLICT (home_team, away_team, match_date)
  DO UPDATE SET score = EXCLUDED.score, updated_at = NOW();

INDEXING:
  Always index columns you filter or join on:
  CREATE INDEX idx_matches_sport ON matches(sport);
  CREATE INDEX idx_odds_match_id ON odds(match_id);
  Unique constraints double as indexes:
  CREATE UNIQUE INDEX uix_match ON matches(home_team, away_team, match_date);

PYTHON + POSTGRESQL (psycopg2):
  import psycopg2

  conn = psycopg2.connect("postgresql://user:password@localhost:5432/dbname")
  cur = conn.cursor()

  cur.execute("SELECT * FROM matches WHERE sport = %s", ("football",))
  rows = cur.fetchall()

  cur.execute(
      "INSERT INTO matches (home_team, away_team) VALUES (%s, %s)",
      ("Arsenal", "Chelsea")
  )
  conn.commit()

SQLALCHEMY (ORM alternative — used with FastAPI):
  from sqlalchemy import create_engine, Column, Integer, String
  from sqlalchemy.orm import declarative_base, Session

  Base = declarative_base()

  class Match(Base):
      __tablename__ = "matches"
      id = Column(Integer, primary_key=True)
      home_team = Column(String, nullable=False)
      away_team = Column(String, nullable=False)

📚 DOCS TO READ:
  https://www.postgresql.org/docs/current/tutorial.html
  https://www.postgresqltutorial.com/
  https://www.psycopg.org/docs/
  https://docs.sqlalchemy.org/en/20/orm/quickstart.html
  https://use-the-index-luke.com/  ← excellent free book on indexing

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 EXERCISES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

These exercises use an in-memory SQLite database (built into Python)
to simulate PostgreSQL. The SQL syntax is ~95% identical for what
we're practising. When you do this for real, just change the
connection string.

NOTE: The SQL you WRITE should be valid PostgreSQL syntax.
      SQLite is just used here so you can run without a server.
"""

import sqlite3
from typing import Any

# ─────────────────────────────────────────────────────────────────
# SETUP — creates a test database (don't modify this)
# ─────────────────────────────────────────────────────────────────

def create_test_db() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.executescript("""
        CREATE TABLE matches (
            id          INTEGER PRIMARY KEY,
            home_team   TEXT NOT NULL,
            away_team   TEXT NOT NULL,
            sport       TEXT NOT NULL,
            match_date  TEXT NOT NULL,
            home_score  INTEGER,
            away_score  INTEGER
        );

        CREATE TABLE odds (
            id          INTEGER PRIMARY KEY,
            match_id    INTEGER NOT NULL,
            home_win    REAL,
            draw        REAL,
            away_win    REAL,
            recorded_at TEXT DEFAULT CURRENT_TIMESTAMP
        );

        INSERT INTO matches VALUES
            (1, 'Arsenal',   'Chelsea',   'football',   '2024-03-10', 2, 1),
            (2, 'Liverpool', 'Man City',  'football',   '2024-03-11', 1, 1),
            (3, 'Djokovic',  'Alcaraz',   'tennis',     '2024-03-12', NULL, NULL),
            (4, 'Arsenal',   'Chelsea',   'football',   '2024-03-10', 2, 1),  -- DUPLICATE
            (5, 'Everton',   'Fulham',    'football',   '2024-03-13', 0, 3),
            (6, 'Lakers',    'Bulls',     'basketball', '2024-03-14', NULL, NULL),
            (7, 'Arsenal',   'Man City',  'football',   '2024-03-15', 1, 2),
            (8, 'Liverpool', 'Chelsea',   'football',   '2024-03-16', 3, 0);

        INSERT INTO odds VALUES
            (1, 1, 1.90, 3.40, 4.20, '2024-03-09 08:00'),
            (2, 1, 1.85, 3.50, 4.50, '2024-03-10 08:00'),
            (3, 2, 2.10, 3.20, 3.50, '2024-03-10 09:00'),
            (4, 5, 3.20, 3.10, 2.20, '2024-03-12 10:00'),
            (5, 7, 2.50, 3.30, 2.80, '2024-03-14 11:00'),
            (6, 8, 1.60, 3.80, 5.50, '2024-03-15 12:00');
    """)
    conn.commit()
    return conn


def run_query(conn: sqlite3.Connection, sql: str, params: tuple = ()) -> list[dict]:
    """Helper to run a query and return results as list of dicts."""
    cur = conn.cursor()
    cur.execute(sql, params)
    return [dict(row) for row in cur.fetchall()]


# ─────────────────────────────────────────────────────────────────
# EXERCISE 1 (Beginner) — Basic queries
# ─────────────────────────────────────────────────────────────────
# Write SQL strings for each query below.

# 1a. All football matches ordered by match_date ascending
QUERY_1A = """
-- YOUR SQL HERE
"""

# 1b. All matches where home_score > away_score (home wins only)
#     Return: home_team, away_team, home_score, away_score
QUERY_1B = """
-- YOUR SQL HERE
"""

# 1c. Count of matches per sport, ordered by count descending
#     Return columns: sport, match_count
QUERY_1C = """
-- YOUR SQL HERE
"""

# 1d. The match with the highest total goals (home_score + away_score)
#     Return all columns for that match
QUERY_1D = """
-- YOUR SQL HERE
"""


# ─────────────────────────────────────────────────────────────────
# EXERCISE 2 (Beginner) — JOINs
# ─────────────────────────────────────────────────────────────────

# 2a. All matches that HAVE odds recorded.
#     Return: match id, home_team, away_team, home_win, draw, away_win
#     (Use only the most recent odds row per match)
#     HINT: Use a subquery or CTE with MAX(recorded_at)
QUERY_2A = """
-- YOUR SQL HERE
"""

# 2b. All matches that do NOT have any odds recorded.
#     Return: match id, home_team, away_team
#     HINT: Use a LEFT JOIN ... WHERE odds.id IS NULL
QUERY_2B = """
-- YOUR SQL HERE
"""


# ─────────────────────────────────────────────────────────────────
# EXERCISE 3 (Intermediate) — Deduplication
# ─────────────────────────────────────────────────────────────────
# Write a Python function `find_duplicates(conn)` that:
#   - Queries the matches table
#   - Returns a list of dicts for any rows considered duplicates
#     (same home_team + away_team + match_date)
#   - Each dict should have: home_team, away_team, match_date, count
#   - Only include groups where count > 1

def find_duplicates(conn: sqlite3.Connection) -> list[dict]:
    sql = """
    -- YOUR SQL HERE
    """
    return run_query(conn, sql)


# Write a function `delete_duplicates(conn)` that:
#   - Deletes duplicate rows, keeping the one with the LOWEST id
#   - Returns the number of rows deleted

def delete_duplicates(conn: sqlite3.Connection) -> int:
    sql = """
    -- YOUR SQL HERE
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.rowcount


# ─────────────────────────────────────────────────────────────────
# EXERCISE 4 (Intermediate) — Aggregates & Window Functions
# ─────────────────────────────────────────────────────────────────

# 4a. For each team that appears as home_team, calculate:
#     - games_played, total_goals_scored, avg_goals_scored
#     Return ordered by avg_goals_scored DESC
#     Only include teams with at least 1 completed game (home_score NOT NULL)
QUERY_4A = """
-- YOUR SQL HERE
"""

# 4b. For match_id=1, show all odds rows with an extra column
#     `prev_home_win` showing the previous odds row's home_win value.
#     Use the LAG() window function.
#     HINT: LAG(home_win, 1) OVER (ORDER BY recorded_at)
QUERY_4B = """
-- YOUR SQL HERE
"""


# ─────────────────────────────────────────────────────────────────
# EXERCISE 5 (Hard) — Schema design
# ─────────────────────────────────────────────────────────────────
# Write the CREATE TABLE SQL for a better version of this database.
# Requirements:
#   - matches table with a UNIQUE constraint on (home_team, away_team, match_date)
#     to prevent duplicates at the DB level
#   - odds table with a foreign key to matches
#   - A `markets` table: id, match_id, market_type (e.g. "match_winner",
#     "over_under_2.5"), is_active (boolean)
#   - Appropriate indexes on columns you'd filter by
#   - Use PostgreSQL types: SERIAL, TIMESTAMP WITH TIME ZONE, BOOLEAN, NUMERIC

SCHEMA_SQL = """
-- YOUR SQL HERE
"""


# ═══════════════════════════════════════════════════════════════════
#  TESTS
# ═══════════════════════════════════════════════════════════════════

def test(description, got, expected):
    status = "✅ PASS" if got == expected else f"❌ FAIL (got {got!r}, expected {expected!r})"
    print(f"  {status}  →  {description}")

conn = create_test_db()

print("\n── Exercise 1: Basic queries ──")
try:
    r = run_query(conn, QUERY_1A)
    test("1a: returns only football",    all(row["sport"] == "football" for row in r if r), True)
    test("1a: ordered by date asc",      r[0]["match_date"] <= r[-1]["match_date"] if len(r) > 1 else True, True)

    r = run_query(conn, QUERY_1B)
    test("1b: only home wins",           all(row["home_score"] > row["away_score"] for row in r), True)
    test("1b: Arsenal win included",     any(row["home_team"] == "Arsenal" for row in r), True)

    r = run_query(conn, QUERY_1C)
    test("1c: has sport column",         "sport" in r[0] if r else False, True)
    test("1c: football is first",        r[0]["sport"] == "football" if r else False, True)

    r = run_query(conn, QUERY_1D)
    test("1d: single row returned",      len(r), 1)
    test("1d: Liverpool match",          r[0]["home_team"] == "Liverpool" if r else False, True)
except Exception as e:
    print(f"  ❌ ERROR: {e}")

print("\n── Exercise 2: JOINs ──")
try:
    r = run_query(conn, QUERY_2A)
    test("2a: matches with odds",        len(r) >= 4, True)
    test("2a: has home_win column",      "home_win" in r[0] if r else False, True)

    r = run_query(conn, QUERY_2B)
    test("2b: matches without odds",     len(r) >= 1, True)
    test("2b: tennis match included",    any("Djokovic" in str(row) for row in r), True)
except Exception as e:
    print(f"  ❌ ERROR: {e}")

print("\n── Exercise 3: Deduplication ──")
try:
    dupes = find_duplicates(conn)
    test("finds 1 duplicate group",     len(dupes), 1)
    test("Arsenal/Chelsea duplicate",   dupes[0]["home_team"] == "Arsenal" if dupes else False, True)
    test("count is 2",                  dupes[0]["count"] == 2 if dupes else False, True)

    deleted = delete_duplicates(conn)
    test("1 row deleted",               deleted, 1)
    dupes_after = find_duplicates(conn)
    test("no duplicates after delete",  len(dupes_after), 0)
except Exception as e:
    print(f"  ❌ ERROR: {e}")

print("\n── Exercise 4: Aggregates & Windows ──")
try:
    r = run_query(conn, QUERY_4A)
    test("4a: has avg_goals_scored col", "avg_goals_scored" in r[0] if r else False, True)
    test("4a: Liverpool top scorer",     r[0]["home_team"] == "Liverpool" if r else False, True)

    r = run_query(conn, QUERY_4B)
    test("4b: has prev_home_win col",   "prev_home_win" in r[0] if r else False, True)
    test("4b: first row prev is NULL",  r[0]["prev_home_win"] is None if r else False, True)
    test("4b: second row has prev val", r[1]["prev_home_win"] == 1.90 if len(r) > 1 else False, True)
except Exception as e:
    print(f"  ❌ ERROR: {e}")

print("\n── Exercise 5: Schema ──")
try:
    has_create = "CREATE TABLE" in SCHEMA_SQL.upper()
    has_unique = "UNIQUE" in SCHEMA_SQL.upper()
    has_fk     = "FOREIGN KEY" in SCHEMA_SQL.upper() or "REFERENCES" in SCHEMA_SQL.upper()
    has_market = "market" in SCHEMA_SQL.lower()
    test("has CREATE TABLE", has_create, True)
    test("has UNIQUE constraint", has_unique, True)
    test("has foreign key reference", has_fk, True)
    test("has markets table", has_market, True)
    print("  ℹ️  Full schema review is manual — paste into https://www.db-fiddle.com to test it")
except Exception as e:
    print(f"  ❌ ERROR: {e}")

print()
