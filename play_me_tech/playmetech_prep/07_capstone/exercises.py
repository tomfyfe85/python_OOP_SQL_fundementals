"""
═══════════════════════════════════════════════════════════════════
 TOPIC 7: CAPSTONE — Mini Sports Data API
═══════════════════════════════════════════════════════════════════

WHY THIS EXISTS:
  Tech tests often ask you to build a small end-to-end system rather
  than isolated functions. This capstone combines everything:
  OOP + pipelines + FastAPI + data quality + SQL patterns.

  Time yourself. A junior engineer should aim to complete
  the core tasks in 2-3 hours.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 THE BRIEF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PlayMeTech wants a small internal REST API that traders can use to:
  1. Ingest match results from a raw data feed (messy, needs cleaning)
  2. Query clean match data with filtering
  3. Submit and retrieve odds for each match
  4. Flag data quality issues automatically

You'll build this in one file using FastAPI + in-memory storage.
No real database needed — use dicts and lists.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 TASKS (in order of difficulty)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TASK 1 — Data models (OOP)
  Build Pydantic models for:
    - RawMatchFeed  : the messy incoming data (see RAW_FEED below)
    - Match         : clean, validated version of a match
    - OddsSubmission: incoming odds from a trader
    - OddsRecord    : stored odds with timestamp + implied probs

TASK 2 — Ingestion pipeline
  Write a function `ingest_feed(raw_records)` that:
    - Parses each raw record into a Match
    - Skips/logs invalid records
    - Deduplicates by (home_team, away_team, match_date)
    - Returns {"ingested": count, "skipped": count, "errors": [details]}

TASK 3 — FastAPI routes
  Build these endpoints:

  POST /ingest
    - Body: list of raw records (RawMatchFeed format)
    - Calls ingest_feed, returns summary

  GET /matches
    - Query params: sport, status, date (all optional)
    - Returns filtered list of Match objects

  GET /matches/{match_id}
    - Returns single match or 404

  POST /matches/{match_id}/odds
    - Body: OddsSubmission
    - Validates odds (all > 1.0)
    - Stores with timestamp
    - Returns 201 with OddsRecord

  GET /matches/{match_id}/odds/latest
    - Returns most recent odds for the match
    - 404 if no odds exist

  GET /matches/{match_id}/odds/history
    - Returns all odds records for the match, oldest first

  GET /quality/report
    - Returns a data quality summary:
      {
        "total_matches": ...,
        "missing_scores": ...,     # matches with no scores yet
        "matches_without_odds": ...,
        "duplicate_attempts_blocked": ...
      }

TASK 4 — (Stretch) Anomaly detection
  - After each POST /matches/{match_id}/odds, check if the new odds
    represent a > 15% move from the previous reading.
  - If so, include a warning in the response:
    {"odds": {...}, "warning": "Large move detected: home_win moved 18%"}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 RAW FEED FORMAT (messy — needs cleaning)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Each raw record looks like this:
{
    "HTeam":  "Arsenal FC",      # home team (may have "FC", "AFC" etc.)
    "ATeam":  "chelsea",         # away team (inconsistent casing)
    "Sport":  "FOOTBALL",        # uppercase
    "Date":   "15/03/2024",      # DD/MM/YYYY format
    "HScore": "2",               # string, may be "" or missing
    "AScore": "1",               # string, may be "" or missing
    "Status": "completed"        # "scheduled", "live", "completed"
}

Cleaning rules:
  - Strip "FC", "AFC", "United" suffixes if they appear alone at the end
    e.g. "Arsenal FC" → "Arsenal", "Leeds United" → "Leeds United" (don't strip if name IS "United")
    Actually: strip " FC" and " AFC" suffixes only. Leave "United" alone.
  - Title-case team names
  - Lowercase sport
  - Parse date from DD/MM/YYYY to a date object
  - Convert scores to int if present, else None
  - Reject records missing HTeam, ATeam, Sport, or Date

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 SAMPLE DATA TO TEST WITH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

SAMPLE_FEED = [
    {"HTeam": "Arsenal FC",  "ATeam": "chelsea",     "Sport": "FOOTBALL", "Date": "15/03/2024", "HScore": "2",  "AScore": "1",  "Status": "completed"},
    {"HTeam": "Liverpool",   "ATeam": "Man City AFC", "Sport": "FOOTBALL", "Date": "16/03/2024", "HScore": "",   "AScore": "",   "Status": "scheduled"},
    {"HTeam": "djokovic",    "ATeam": "ALCARAZ",      "Sport": "TENNIS",   "Date": "17/03/2024", "HScore": None, "AScore": None, "Status": "live"},
    {"HTeam": "Arsenal FC",  "ATeam": "chelsea",      "Sport": "FOOTBALL", "Date": "15/03/2024", "HScore": "2",  "AScore": "1",  "Status": "completed"},  # DUPLICATE
    {"HTeam": "",            "ATeam": "Fulham",       "Sport": "FOOTBALL", "Date": "18/03/2024", "HScore": "0",  "AScore": "3",  "Status": "completed"},  # INVALID: no home team
    {"HTeam": "Everton",     "ATeam": "Fulham",       "Sport": "FOOTBALL", "Date": "18/03/2024", "HScore": "0",  "AScore": "3",  "Status": "completed"},
]

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 BUILD YOUR SOLUTION BELOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# Imports you'll likely need:
from datetime import datetime, date, timezone
from typing import Optional
import logging
import uuid

# YOUR CODE HERE
# ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓


"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 TESTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

try:
    from fastapi.testclient import TestClient
    FASTAPI_AVAILABLE = True
except ImportError:
    FASTAPI_AVAILABLE = False
    print("⚠️  Install FastAPI first: pip install fastapi httpx\n")

def test(description, got, expected):
    status = "✅ PASS" if got == expected else f"❌ FAIL (got {got!r}, expected {expected!r})"
    print(f"  {status}  →  {description}")

if FASTAPI_AVAILABLE:
    try:
        client = TestClient(app)  # assumes your FastAPI app is called `app`

        print("\n── Task 2 & 3: Ingestion ──")
        r = client.post("/ingest", json=SAMPLE_FEED)
        test("ingest status 200",           r.status_code, 200)
        test("4 matches ingested",          r.json().get("ingested"), 4)
        test("1 duplicate blocked",         r.json().get("skipped", 0) >= 1, True)
        test("1 invalid skipped",           len(r.json().get("errors", [])) >= 1, True)

        print("\n── Task 3: GET /matches ──")
        r = client.get("/matches")
        test("returns matches",             len(r.json()) >= 4, True)

        r = client.get("/matches?sport=football")
        test("filter by sport",             all(m["sport"] == "football" for m in r.json()), True)

        print("\n── Task 3: Data cleaning ──")
        r = client.get("/matches")
        teams = [m["home_team"] for m in r.json()]
        test("Arsenal FC cleaned",          "Arsenal" in teams, True)
        test("Man City AFC cleaned",        any("Man City" in t for t in [m["away_team"] for m in r.json()]), True)
        test("title case applied",          all(t[0].isupper() for t in teams if t), True)

        print("\n── Task 3: Odds ──")
        r = client.get("/matches")
        match_id = r.json()[0]["id"]

        odds_payload = {"home_win": 1.9, "draw": 3.4, "away_win": 4.2}
        r = client.post(f"/matches/{match_id}/odds", json=odds_payload)
        test("post odds 201",               r.status_code, 201)
        test("implied probs present",       "implied_probabilities" in r.json(), True)

        r = client.get(f"/matches/{match_id}/odds/latest")
        test("get latest odds 200",         r.status_code, 200)

        r = client.get(f"/matches/{match_id}/odds/history")
        test("history is list",             isinstance(r.json(), list), True)

        r = client.get("/matches/nonexistent-id/odds/latest")
        test("404 for no odds",             r.status_code, 404)

        print("\n── Task 3: Quality report ──")
        r = client.get("/quality/report")
        test("quality report 200",          r.status_code, 200)
        test("has total_matches",           "total_matches" in r.json(), True)
        test("has missing_scores",          "missing_scores" in r.json(), True)
        test("has matches_without_odds",    "matches_without_odds" in r.json(), True)

        print("\n── Task 4 (Stretch): Anomaly detection ──")
        odds2 = {"home_win": 1.5, "draw": 3.4, "away_win": 4.2}  # big drop from 1.9
        r = client.post(f"/matches/{match_id}/odds", json=odds2)
        has_warning = "warning" in r.json()
        test("anomaly warning present",     has_warning, True)

    except NameError:
        print("  ⚠️  `app` not defined — build your FastAPI app and assign it to `app`")
    except Exception as e:
        print(f"  ❌ ERROR: {e}")

print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 SELF-REVIEW CHECKLIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 After all tests pass, review your own code:

 □ Are my class/function names clear and descriptive?
 □ Do my functions do ONE thing each?
 □ Have I handled all error cases (missing data, bad types, 404s)?
 □ Are my Pydantic models doing the validation, or am I doing it manually?
 □ Would a trader understand what each API endpoint returns?
 □ If someone ran this twice with the same data, does it behave sensibly?
 □ Have I used logging instead of print() for operational messages?
""")
