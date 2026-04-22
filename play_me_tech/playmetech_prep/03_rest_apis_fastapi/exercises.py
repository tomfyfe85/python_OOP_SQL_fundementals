"""
═══════════════════════════════════════════════════════════════════
 TOPIC 3: REST APIs with FastAPI
═══════════════════════════════════════════════════════════════════

WHY THIS MATTERS FOR PLAYMETECH:
  The role mentions building "web-based control consoles" and the
  job spec asks for "basic understanding of APIs (REST)." FastAPI
  is modern, fast, and used extensively in Python data teams.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 THEORY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

REST (Representational State Transfer) is a style for designing APIs.
The key idea: resources are nouns, HTTP methods are verbs.

HTTP METHODS:
  GET     → Read data (safe, no side effects)
  POST    → Create a new resource
  PUT     → Replace a resource entirely
  PATCH   → Update part of a resource
  DELETE  → Remove a resource

STATUS CODES TO KNOW:
  200 OK           → success
  201 Created      → resource was created
  204 No Content   → success, nothing to return
  400 Bad Request  → client sent invalid data
  404 Not Found    → resource doesn't exist
  422 Unprocessable Entity → validation failed (FastAPI uses this a lot)
  500 Internal Server Error → something broke server-side

FASTAPI BASICS:
  from fastapi import FastAPI, HTTPException
  from pydantic import BaseModel

  app = FastAPI()

  class Item(BaseModel):
      name: str
      price: float

  @app.get("/items/{item_id}")
  def get_item(item_id: int):
      return {"id": item_id, "name": "example"}

  @app.post("/items/", status_code=201)
  def create_item(item: Item):
      return item

  # Run with: uvicorn filename:app --reload

PATH PARAMETERS vs QUERY PARAMETERS:
  Path:  /matches/{match_id}        → required, part of URL
  Query: /matches?sport=football     → optional filter

  @app.get("/matches/{match_id}")
  def get_match(match_id: int, include_odds: bool = False):
      # match_id is from path, include_odds is from query string
      ...

DEPENDENCY INJECTION (intermediate):
  FastAPI supports injecting shared resources (db connections, auth)
  using Depends(). This keeps routes clean.

  from fastapi import Depends

  def get_db():
      db = connect()
      try:
          yield db
      finally:
          db.close()

  @app.get("/matches")
  def list_matches(db = Depends(get_db)):
      return db.query_all()

📚 DOCS TO READ:
  https://fastapi.tiangolo.com/tutorial/
  https://fastapi.tiangolo.com/tutorial/path-params/
  https://fastapi.tiangolo.com/tutorial/query-params/
  https://fastapi.tiangolo.com/tutorial/body/
  https://fastapi.tiangolo.com/tutorial/response-model/

TO INSTALL:
  pip install fastapi uvicorn httpx

TO TEST WITHOUT A REAL SERVER (used in exercises below):
  from fastapi.testclient import TestClient
  client = TestClient(app)
  response = client.get("/matches/1")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 EXERCISES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NOTE: These exercises use FastAPI's TestClient so you can run them
without starting a server. Install: pip install fastapi httpx
"""

try:
    from fastapi import FastAPI, HTTPException, Query
    from fastapi.testclient import TestClient
    from pydantic import BaseModel, Field, validator
    FASTAPI_AVAILABLE = True
except ImportError:
    print("⚠️  FastAPI not installed. Run: pip install fastapi httpx")
    print("   Exercises will be skipped but you can still read the theory above.\n")
    FASTAPI_AVAILABLE = False

# ─────────────────────────────────────────────────────────────────
# SHARED IN-MEMORY "DATABASE" (stands in for a real DB)
# ─────────────────────────────────────────────────────────────────

MATCHES_DB: dict = {
    1: {"id": 1, "home_team": "Arsenal",   "away_team": "Chelsea",   "sport": "football", "status": "scheduled"},
    2: {"id": 2, "home_team": "Djokovic",  "away_team": "Alcaraz",   "sport": "tennis",   "status": "live"},
    3: {"id": 3, "home_team": "Liverpool", "away_team": "Man City",  "sport": "football", "status": "completed"},
}


# ─────────────────────────────────────────────────────────────────
# EXERCISE 1 (Beginner) — GET endpoints
# ─────────────────────────────────────────────────────────────────
# Build a FastAPI app with two GET routes:
#
#   GET /matches
#     - Returns all matches from MATCHES_DB as a list
#     - Optional query param: sport (str) — filter by sport if provided
#     - Optional query param: status (str) — filter by status if provided
#
#   GET /matches/{match_id}
#     - Returns a single match by ID
#     - Returns 404 if not found (use HTTPException)

app_ex1 = FastAPI()

# YOUR CODE HERE


# ─────────────────────────────────────────────────────────────────
# EXERCISE 2 (Beginner) — POST with validation
# ─────────────────────────────────────────────────────────────────
# Define a Pydantic model `CreateMatchRequest` with fields:
#   home_team: str  (must not be empty)
#   away_team: str  (must not be empty)
#   sport: str      (must be one of: "football", "tennis", "basketball")
#
# Build an app with:
#   POST /matches
#     - Accepts a CreateMatchRequest body
#     - Assigns a new ID (max existing ID + 1)
#     - Adds the match to MATCHES_DB_2 (use a fresh copy below)
#     - Returns the created match with status 201
#
#   FastAPI handles validation automatically — if sport is invalid,
#   it will return 422 without you writing any error handling code.
#   Try to trigger this in the tests!

import copy
MATCHES_DB_2 = copy.deepcopy(MATCHES_DB)

app_ex2 = FastAPI()

class CreateMatchRequest(BaseModel):
    # YOUR CODE HERE
    pass

# YOUR ROUTES HERE


# ─────────────────────────────────────────────────────────────────
# EXERCISE 3 (Intermediate) — PATCH & DELETE
# ─────────────────────────────────────────────────────────────────
# Using a fresh DB copy, add PATCH and DELETE routes:
#
#   PATCH /matches/{match_id}/status
#     - Body: {"status": "live"} or {"status": "completed"}
#     - Updates only the status field
#     - Returns the updated match
#     - 404 if match not found
#     - 400 if status value is invalid
#
#   DELETE /matches/{match_id}
#     - Removes the match
#     - Returns 204 No Content on success
#     - Returns 404 if not found

import copy
MATCHES_DB_3 = copy.deepcopy(MATCHES_DB)

app_ex3 = FastAPI()

class UpdateStatusRequest(BaseModel):
    # YOUR CODE HERE
    pass

# YOUR ROUTES HERE


# ─────────────────────────────────────────────────────────────────
# EXERCISE 4 (Hard) — Design a mini odds API
# ─────────────────────────────────────────────────────────────────
# Design and build an API a trader would actually use.
# No stubs — this is open-ended. You decide the models.
#
# Requirements:
#   - GET  /odds/{match_id}
#       Returns current odds for a match (home_win, draw, away_win)
#       Include the implied probability for each outcome
#       Include a "favourite" field
#       404 if match not found
#
#   - POST /odds/{match_id}
#       Accepts new odds for a match
#       Validates: all odds must be > 1.0 (otherwise 400)
#       Stores them in ODDS_DB (defined below)
#       Returns 201 with the stored odds
#
#   - GET /odds/{match_id}/history
#       Returns a list of all odds updates for that match in order
#       Returns [] if no history yet

from datetime import datetime

ODDS_DB: dict[int, list[dict]] = {}  # match_id → list of odds snapshots

app_ex4 = FastAPI()

# YOUR CODE HERE


# ═══════════════════════════════════════════════════════════════════
#  TESTS
# ═══════════════════════════════════════════════════════════════════

def test(description, got, expected):
    status = "✅ PASS" if got == expected else f"❌ FAIL (got {got!r}, expected {expected!r})"
    print(f"  {status}  →  {description}")

if not FASTAPI_AVAILABLE:
    print("Skipping tests — install FastAPI first.\n")
else:
    print("\n── Exercise 1: GET /matches ──")
    try:
        client = TestClient(app_ex1)
        r = client.get("/matches")
        test("status 200",           r.status_code, 200)
        test("returns 3 matches",    len(r.json()), 3)

        r = client.get("/matches?sport=football")
        test("filter by sport",      len(r.json()), 2)

        r = client.get("/matches?status=live")
        test("filter by status",     len(r.json()), 1)

        r = client.get("/matches/1")
        test("single match",         r.json()["home_team"], "Arsenal")

        r = client.get("/matches/999")
        test("404 for missing",      r.status_code, 404)
    except Exception as e:
        print(f"  ❌ ERROR: {e}")

    print("\n── Exercise 2: POST /matches ──")
    try:
        client = TestClient(app_ex2)
        payload = {"home_team": "Everton", "away_team": "Fulham", "sport": "football"}
        r = client.post("/matches", json=payload)
        test("status 201",           r.status_code, 201)
        test("id assigned",          "id" in r.json(), True)
        test("correct home team",    r.json()["home_team"], "Everton")

        bad = {"home_team": "X", "away_team": "Y", "sport": "cricket"}
        r = client.post("/matches", json=bad)
        test("invalid sport → 422",  r.status_code, 422)
    except Exception as e:
        print(f"  ❌ ERROR: {e}")

    print("\n── Exercise 3: PATCH & DELETE ──")
    try:
        client = TestClient(app_ex3)
        r = client.patch("/matches/1/status", json={"status": "live"})
        test("patch status 200",     r.status_code, 200)
        test("status updated",       r.json()["status"], "live")

        r = client.patch("/matches/1/status", json={"status": "invalid"})
        test("invalid status → 400", r.status_code, 400)

        r = client.delete("/matches/2")
        test("delete status 204",    r.status_code, 204)

        r = client.get("/matches/2") if hasattr(app_ex3, 'routes') else None
        r2 = client.delete("/matches/999")
        test("delete 404 for missing", r2.status_code, 404)
    except Exception as e:
        print(f"  ❌ ERROR: {e}")

    print("\n── Exercise 4: Odds API ──")
    try:
        client = TestClient(app_ex4)

        r = client.get("/odds/1")
        test("404 before any odds posted", r.status_code, 404)

        odds_payload = {"home_win": 1.9, "draw": 3.4, "away_win": 4.2}
        r = client.post("/odds/1", json=odds_payload)
        test("post odds 201",        r.status_code, 201)

        r = client.get("/odds/1")
        test("get odds 200",         r.status_code, 200)
        test("favourite in response","favourite" in r.json(), True)
        test("implied probs present","implied_probabilities" in r.json(), True)

        bad_odds = {"home_win": 0.5, "draw": 3.4, "away_win": 4.2}
        r = client.post("/odds/1", json=bad_odds)
        test("odds <= 1.0 rejected", r.status_code, 400)

        client.post("/odds/1", json={"home_win": 2.0, "draw": 3.0, "away_win": 3.5})
        r = client.get("/odds/1/history")
        test("history returns list", isinstance(r.json(), list), True)
        test("history has 2 entries", len(r.json()), 2)
    except Exception as e:
        print(f"  ❌ ERROR: {e}")

    print()
