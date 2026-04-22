"""
═══════════════════════════════════════════════════════════════════
 TOPIC 2: Data Pipelines — Scraping, Transforming & Storing
═══════════════════════════════════════════════════════════════════

WHY THIS MATTERS FOR PLAYMETECH:
  The role explicitly involves "end-to-end sports data pipelines —
  scraping, cleaning, transformation, and reliable data storage."
  This is the core engineering work you'll do day-to-day.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 THEORY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A DATA PIPELINE is a series of steps that moves data from a source
to a destination, transforming it along the way:

  [Source] → [Extract] → [Transform] → [Load] → [Destination]
                              ETL

EXTRACT (getting the data):
  - HTTP requests to APIs: requests.get(url)
  - HTML scraping:         BeautifulSoup, httpx
  - Pagination:            loop until no "next page" token

TRANSFORM (cleaning & reshaping):
  - Parse raw strings into typed values (float, datetime, etc.)
  - Normalise inconsistent naming ("Man Utd" vs "Manchester United")
  - Deduplicate records
  - Filter out invalid/incomplete rows

LOAD (storing the data):
  - Insert into PostgreSQL
  - Append to a CSV / Parquet file
  - Publish to a message queue

ROBUSTNESS PATTERNS:
  - Retry on failure      → use tenacity or manual retry loops
  - Log every step        → use Python's logging module, not print()
  - Idempotency           → running the pipeline twice produces the
                            same result (use INSERT ... ON CONFLICT)
  - Schema validation     → reject bad records early (use pydantic)

PYTHON TOOLS YOU SHOULD KNOW:
  requests   → HTTP calls (pip install requests)
  httpx      → async HTTP (pip install httpx)
  pydantic   → data validation & parsing (pip install pydantic)
  logging    → structured log output (built-in)
  datetime   → date/time parsing (built-in)
  csv        → reading/writing CSV files (built-in)

PYDANTIC QUICK EXAMPLE:
  from pydantic import BaseModel, validator

  class MatchResult(BaseModel):
      home_team: str
      away_team: str
      home_score: int
      away_score: int

      @validator("home_score", "away_score")
      def score_non_negative(cls, v):
          if v < 0:
              raise ValueError("Score cannot be negative")
          return v

  result = MatchResult(home_team="Arsenal", away_team="Chelsea",
                        home_score=2, away_score=1)

📚 DOCS TO READ:
  https://docs.python-requests.org/en/latest/
  https://docs.pydantic.dev/latest/
  https://docs.python.org/3/library/logging.html
  https://docs.python.org/3/library/csv.html
  https://realpython.com/python-logging/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 EXERCISES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

import csv
import io
import logging
import json
from datetime import datetime
from typing import Optional

# ─────────────────────────────────────────────────────────────────
# EXERCISE 1 (Beginner) — Parsing raw data
# ─────────────────────────────────────────────────────────────────
# The raw_records list below simulates data scraped from a web page.
# Write a function `parse_records(raw_records)` that:
#   - Converts "home_score" and "away_score" to ints
#   - Converts "date" strings to datetime.date objects (format: YYYY-MM-DD)
#   - Skips any record where scores are missing or can't be parsed
#   - Returns a list of clean dicts

RAW_RECORDS = [
    {"home_team": "Arsenal",   "away_team": "Chelsea",  "home_score": "2", "away_score": "1",  "date": "2024-03-15"},
    {"home_team": "Liverpool", "away_team": "Man City",  "home_score": "",  "away_score": "2",  "date": "2024-03-16"},
    {"home_team": "Spurs",     "away_team": "West Ham",  "home_score": "0", "away_score": "abc","date": "2024-03-17"},
    {"home_team": "Everton",   "away_team": "Fulham",    "home_score": "1", "away_score": "1",  "date": "2024-03-18"},
]

def parse_records(raw_records: list[dict]) -> list[dict]:
    # YOUR CODE HERE
    pass


# ─────────────────────────────────────────────────────────────────
# EXERCISE 2 (Beginner) — Deduplication
# ─────────────────────────────────────────────────────────────────
# Pipelines often receive duplicate records (same API called twice,
# retry that succeeded after a partial insert, etc.)
#
# Write `deduplicate(records, key_fields)` that:
#   - Takes a list of dicts and a list of field names that form a unique key
#   - Returns a list with duplicates removed, keeping the LAST occurrence
#
# Example: key_fields=["home_team", "away_team", "date"]
#   If two records have the same home/away/date, keep the later one.

def deduplicate(records: list[dict], key_fields: list[str]) -> list[dict]:
    # YOUR CODE HERE
    pass


# ─────────────────────────────────────────────────────────────────
# EXERCISE 3 (Intermediate) — CSV pipeline
# ─────────────────────────────────────────────────────────────────
# Write a function `csv_pipeline(csv_string)` that:
#   1. Reads the CSV data from the string below
#   2. Parses each row (convert odds columns to float, skip bad rows)
#   3. Adds a computed column: "overround" = sum of implied probs
#      implied_prob = 1 / decimal_odds, overround > 1.0 means bookmaker edge
#   4. Returns a list of clean dicts with the overround field added
#
# HINT: use the csv module, io.StringIO to read from a string

CSV_DATA = """match_id,home_odds,draw_odds,away_odds
1,1.90,3.40,4.20
2,2.10,bad_data,3.50
3,1.50,4.00,6.00
4,2.80,3.10,2.60
"""

def csv_pipeline(csv_string: str) -> list[dict]:
    # YOUR CODE HERE
    pass


# ─────────────────────────────────────────────────────────────────
# EXERCISE 4 (Intermediate) — Retry logic
# ─────────────────────────────────────────────────────────────────
# Real pipelines hit flaky APIs. Write a `retry(func, max_attempts, delay_secs)`
# function that:
#   - Calls func()
#   - If it raises an exception, waits delay_secs then tries again
#   - After max_attempts failures, raises the last exception
#   - Returns the result if successful
#
# For the delay, import time and use time.sleep(delay_secs)
# Log each retry attempt using the logging module (logging.warning)
#
# BONUS: make it accept an optional `exceptions` tuple so it only
# retries on specific exception types (default: retry on any Exception)

import time

def retry(func, max_attempts: int = 3, delay_secs: float = 1.0, exceptions: tuple = (Exception,)):
    # YOUR CODE HERE
    pass


# ─────────────────────────────────────────────────────────────────
# EXERCISE 5 (Hard) — Build a mini ETL pipeline class
# ─────────────────────────────────────────────────────────────────
# Build a Pipeline class that chains steps together.
# Each step is a function that takes a list of records and returns a list.
#
# The class should:
#   - __init__(self, name: str)  — store the pipeline name
#   - add_step(self, fn)         — register a processing function
#   - run(self, records: list)   — run all steps in order, passing
#                                  output of each step into the next
#   - Log (using logging.info) before and after each step, including
#     how many records entered and how many came out
#
# Example usage:
#   pipeline = Pipeline("scores_pipeline")
#   pipeline.add_step(remove_nulls)
#   pipeline.add_step(normalise_team_names)
#   results = pipeline.run(raw_data)

class Pipeline:
    # YOUR CODE HERE
    pass


# ═══════════════════════════════════════════════════════════════════
#  TESTS
# ═══════════════════════════════════════════════════════════════════

def test(description, got, expected):
    status = "✅ PASS" if got == expected else f"❌ FAIL (got {got!r}, expected {expected!r})"
    print(f"  {status}  →  {description}")

print("\n── Exercise 1: parse_records ──")
try:
    result = parse_records(RAW_RECORDS)
    test("only valid records returned", len(result), 2)
    test("scores are ints",  isinstance(result[0]["home_score"], int), True)
    test("date is date obj", isinstance(result[0]["date"], __import__("datetime").date), True)
    test("correct teams",    result[0]["home_team"], "Arsenal")
except Exception as e:
    print(f"  ❌ ERROR: {e}")

print("\n── Exercise 2: deduplicate ──")
try:
    dupes = [
        {"home": "Arsenal", "away": "Chelsea", "date": "2024-01-01", "source": "feed_a"},
        {"home": "Arsenal", "away": "Chelsea", "date": "2024-01-01", "source": "feed_b"},
        {"home": "Liverpool", "away": "Everton", "date": "2024-01-02", "source": "feed_a"},
    ]
    result = deduplicate(dupes, ["home", "away", "date"])
    test("correct count", len(result), 2)
    test("keeps last occurrence", result[0]["source"], "feed_b")
except Exception as e:
    print(f"  ❌ ERROR: {e}")

print("\n── Exercise 3: csv_pipeline ──")
try:
    result = csv_pipeline(CSV_DATA)
    test("skips bad row",        len(result), 3)
    test("odds are floats",      isinstance(result[0]["home_odds"], float), True)
    test("overround computed",   "overround" in result[0], True)
    test("overround > 1",        result[0]["overround"] > 1.0, True)
    test("overround reasonable", result[0]["overround"] < 1.2, True)  # shouldn't be crazy high
except Exception as e:
    print(f"  ❌ ERROR: {e}")

print("\n── Exercise 4: retry ──")
try:
    call_count = {"n": 0}

    def flaky():
        call_count["n"] += 1
        if call_count["n"] < 3:
            raise ConnectionError("timeout")
        return "success"

    result = retry(flaky, max_attempts=3, delay_secs=0)
    test("succeeds on 3rd attempt", result, "success")
    test("called 3 times", call_count["n"], 3)

    def always_fails():
        raise ValueError("nope")

    try:
        retry(always_fails, max_attempts=2, delay_secs=0)
        test("raises after max attempts", False, True)
    except ValueError:
        test("raises after max attempts", True, True)
except Exception as e:
    print(f"  ❌ ERROR: {e}")

print("\n── Exercise 5: Pipeline ──")
try:
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    def keep_high_scores(records):
        return [r for r in records if r.get("score", 0) > 2]

    def add_label(records):
        for r in records:
            r["label"] = f"score:{r['score']}"
        return records

    data = [{"score": 1}, {"score": 3}, {"score": 5}]
    p = Pipeline("test_pipeline")
    p.add_step(keep_high_scores)
    p.add_step(add_label)
    result = p.run(data)
    test("pipeline filters correctly",  len(result), 2)
    test("pipeline transforms correctly", result[0]["label"], "score:3")
except Exception as e:
    print(f"  ❌ ERROR: {e}")

print()
