"""
═══════════════════════════════════════════════════════════════════
 TOPIC 6: Data Quality — Validation, Error Handling & Alerting
═══════════════════════════════════════════════════════════════════

WHY THIS MATTERS FOR PLAYMETECH:
  "Monitor, investigate, and troubleshoot data quality issues such
  as missing, inconsistent, or duplicated records" is a direct quote
  from the job spec. Bad data = bad trading decisions = real losses.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 THEORY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DATA QUALITY DIMENSIONS:
  COMPLETENESS  → Are required fields present? No nulls where not allowed?
  VALIDITY      → Do values conform to expected ranges/formats/types?
  CONSISTENCY   → Does data agree across sources? (odds from two feeds match?)
  TIMELINESS    → Is data fresh? Or is it stale from hours ago?
  UNIQUENESS    → No duplicate records?
  ACCURACY      → Does the data reflect reality? (harder to test automatically)

VALIDATION APPROACHES:

  1. SCHEMA VALIDATION (Pydantic) — catch bad types/shapes on ingestion
     from pydantic import BaseModel, validator, Field

     class OddsRecord(BaseModel):
         match_id: int
         home_win: float = Field(gt=1.0)   # must be > 1.0
         draw: float     = Field(gt=1.0)
         away_win: float = Field(gt=1.0)
         timestamp: datetime

  2. BUSINESS RULE VALIDATION — domain-specific checks after ingestion
     - Implied probabilities shouldn't exceed 115% (overround cap)
     - Score can't be negative
     - Match can't start before today if status is "scheduled"

  3. ANOMALY DETECTION — flag unusual values for human review
     - Odds moved > 20% in 5 minutes → alert
     - Zero records returned from a scrape → alert
     - Scrape ran but took 10x longer than usual → alert

STRUCTURED EXCEPTION HANDLING:
  Create a hierarchy of custom exceptions for clarity:

  class DataPipelineError(Exception):
      """Base for all pipeline errors."""

  class ValidationError(DataPipelineError):
      """Record failed validation."""
      def __init__(self, field: str, value, reason: str):
          self.field = field
          self.value = value
          self.reason = reason
          super().__init__(f"Validation failed for {field}={value!r}: {reason}")

  class StaleDataError(DataPipelineError):
      """Data is too old to be trusted."""

RESULT PATTERN (process bad records without crashing everything):
  Instead of raising on the first bad record and stopping the whole
  pipeline, collect errors alongside successes:

  results = {"success": [], "errors": []}

  for record in records:
      try:
          clean = validate(record)
          results["success"].append(clean)
      except ValidationError as e:
          results["errors"].append({"record": record, "error": str(e)})

  # Log a summary, alert if error rate is too high
  error_rate = len(results["errors"]) / len(records)
  if error_rate > 0.05:
      alert(f"High error rate: {error_rate:.1%}")

📚 DOCS TO READ:
  https://docs.pydantic.dev/latest/concepts/validators/
  https://docs.python.org/3/tutorial/errors.html
  https://docs.python.org/3/library/logging.html
  https://realpython.com/python-exceptions/
  https://realpython.com/python-type-checking/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 EXERCISES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

from datetime import datetime, timedelta, timezone
from typing import Optional
import logging

logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s")

# ─────────────────────────────────────────────────────────────────
# EXERCISE 1 (Beginner) — Custom exception hierarchy
# ─────────────────────────────────────────────────────────────────
# Create an exception hierarchy for a data pipeline:
#
#   DataPipelineError (base)
#   ├── ValidationError  — a record failed a validation rule
#   │     attrs: field (str), value (any), reason (str)
#   │     __str__ → "Validation failed: <field>=<value> — <reason>"
#   ├── StaleDataError   — data is too old
#   │     attrs: source (str), age_seconds (float)
#   │     __str__ → "Stale data from <source>: <age>s old"
#   └── DuplicateRecordError — record already exists
#         attrs: key (str)
#         __str__ → "Duplicate record with key: <key>"

class DataPipelineError(Exception):
    # YOUR CODE HERE
    pass

class ValidationError(DataPipelineError):
    # YOUR CODE HERE
    pass

class StaleDataError(DataPipelineError):
    # YOUR CODE HERE
    pass

class DuplicateRecordError(DataPipelineError):
    # YOUR CODE HERE
    pass


# ─────────────────────────────────────────────────────────────────
# EXERCISE 2 (Beginner) — Validation function
# ─────────────────────────────────────────────────────────────────
# Write `validate_odds_record(record: dict) -> dict` that:
#   - Checks "match_id" is present and is an int > 0
#   - Checks "home_win", "draw", "away_win" are all present and float > 1.0
#   - Checks overround (sum of implied probs) is < 1.20
#   - Raises ValidationError for the FIRST failing check it finds
#   - Returns the record dict unchanged if all checks pass
#   - Converts string numbers to float if needed (e.g. "1.9" → 1.9)

def validate_odds_record(record: dict) -> dict:
    # YOUR CODE HERE
    pass


# ─────────────────────────────────────────────────────────────────
# EXERCISE 3 (Intermediate) — Batch processor with error collection
# ─────────────────────────────────────────────────────────────────
# Write `process_batch(records: list[dict]) -> dict` that:
#   - Runs validate_odds_record on each record
#   - Collects results into {"success": [...], "errors": [...]}
#   - Error entries: {"record": original_record, "error": error_message_str}
#   - After processing, logs a WARNING if error_rate > 10%
#   - Returns the results dict

def process_batch(records: list[dict]) -> dict:
    # YOUR CODE HERE
    pass


# ─────────────────────────────────────────────────────────────────
# EXERCISE 4 (Intermediate) — Staleness check
# ─────────────────────────────────────────────────────────────────
# Write `check_freshness(records: list[dict], max_age_seconds: int) -> list[dict]`
#   - Each record has a "timestamp" key (datetime object, UTC)
#   - Returns only records where now - timestamp <= max_age_seconds
#   - Raises StaleDataError if ALL records are stale (nothing to return)
#   - Logs a WARNING for each stale record it drops

def check_freshness(records: list[dict], max_age_seconds: int) -> list[dict]:
    # YOUR CODE HERE
    pass


# ─────────────────────────────────────────────────────────────────
# EXERCISE 5 (Hard) — Anomaly detector
# ─────────────────────────────────────────────────────────────────
# In live sports trading, odds move constantly. A sudden large move
# can indicate a data error OR a real market signal. Either way, you
# want to know about it.
#
# Write a class `OddsAnomalyDetector`:
#   - __init__(self, threshold_pct: float = 0.15)
#       stores the % change that triggers an alert (default 15%)
#
#   - record(self, match_id: int, outcome: str, odds: float, timestamp: datetime)
#       stores the reading. outcome is e.g. "home_win", "draw", "away_win"
#
#   - check_for_anomalies(self) -> list[dict]
#       For each (match_id, outcome) pair, compare consecutive readings.
#       If the % change between two consecutive readings exceeds threshold_pct,
#       add an anomaly dict to the results:
#       {
#           "match_id": ...,
#           "outcome": ...,
#           "prev_odds": ...,
#           "new_odds": ...,
#           "change_pct": ...,   # e.g. 0.18 for 18%
#           "timestamp": ...     # timestamp of the new reading
#       }
#       Return all anomalies found.
#
#   - HINT: % change = abs(new - old) / old

class OddsAnomalyDetector:
    # YOUR CODE HERE
    pass


# ═══════════════════════════════════════════════════════════════════
#  TESTS
# ═══════════════════════════════════════════════════════════════════

def test(description, got, expected):
    status = "✅ PASS" if got == expected else f"❌ FAIL (got {got!r}, expected {expected!r})"
    print(f"  {status}  →  {description}")

print("\n── Exercise 1: Exception hierarchy ──")
try:
    e = ValidationError("home_win", 0.5, "must be > 1.0")
    test("ValidationError str",    "Validation failed" in str(e), True)
    test("ValidationError field",  e.field, "home_win")
    test("is DataPipelineError",   isinstance(e, DataPipelineError), True)

    e2 = StaleDataError("feed_a", 3720.0)
    test("StaleDataError str",     "Stale data" in str(e2), True)
    test("is DataPipelineError",   isinstance(e2, DataPipelineError), True)

    e3 = DuplicateRecordError("match_1_2024-03-10")
    test("DuplicateRecordError",   "Duplicate" in str(e3), True)
except Exception as e:
    print(f"  ❌ ERROR: {e}")

print("\n── Exercise 2: validate_odds_record ──")
try:
    valid = {"match_id": 1, "home_win": 1.9, "draw": 3.4, "away_win": 4.2}
    result = validate_odds_record(valid)
    test("valid record passes",    result == valid, True)

    # String numbers should be accepted
    string_odds = {"match_id": 1, "home_win": "1.9", "draw": "3.4", "away_win": "4.2"}
    result2 = validate_odds_record(string_odds)
    test("string odds converted",  isinstance(result2["home_win"], float), True)

    # Missing field
    try:
        validate_odds_record({"match_id": 1, "home_win": 1.9})
        test("missing field raises", False, True)
    except ValidationError:
        test("missing field raises", True, True)

    # Odds <= 1.0
    try:
        validate_odds_record({"match_id": 1, "home_win": 0.5, "draw": 3.4, "away_win": 4.2})
        test("odds <= 1.0 raises",  False, True)
    except ValidationError:
        test("odds <= 1.0 raises",  True, True)

    # Overround too high
    try:
        validate_odds_record({"match_id": 1, "home_win": 1.01, "draw": 1.01, "away_win": 1.01})
        test("high overround raises", False, True)
    except ValidationError:
        test("high overround raises", True, True)
except Exception as e:
    print(f"  ❌ ERROR: {e}")

print("\n── Exercise 3: process_batch ──")
try:
    batch = [
        {"match_id": 1, "home_win": 1.9, "draw": 3.4, "away_win": 4.2},
        {"match_id": 2, "home_win": 0.5, "draw": 3.4, "away_win": 4.2},  # invalid
        {"match_id": 3, "home_win": 2.0, "draw": 3.0, "away_win": 3.5},
        {"match_id": 4},                                                    # missing
    ]
    result = process_batch(batch)
    test("2 successes",            len(result["success"]), 2)
    test("2 errors",               len(result["errors"]),  2)
    test("error has 'error' key",  "error" in result["errors"][0], True)
    test("error has 'record' key", "record" in result["errors"][0], True)
except Exception as e:
    print(f"  ❌ ERROR: {e}")

print("\n── Exercise 4: check_freshness ──")
try:
    now = datetime.now(timezone.utc)
    records = [
        {"id": 1, "timestamp": now - timedelta(seconds=30)},   # fresh
        {"id": 2, "timestamp": now - timedelta(seconds=200)},  # stale
        {"id": 3, "timestamp": now - timedelta(seconds=50)},   # fresh
    ]
    result = check_freshness(records, max_age_seconds=60)
    test("2 fresh records returned", len(result), 2)
    test("fresh ids correct",        {r["id"] for r in result}, {1, 3})

    try:
        check_freshness([{"id": 1, "timestamp": now - timedelta(seconds=500)}], 60)
        test("all stale raises StaleDataError", False, True)
    except StaleDataError:
        test("all stale raises StaleDataError", True, True)
except Exception as e:
    print(f"  ❌ ERROR: {e}")

print("\n── Exercise 5: OddsAnomalyDetector ──")
try:
    detector = OddsAnomalyDetector(threshold_pct=0.10)
    t = datetime.now(timezone.utc)

    detector.record(1, "home_win", 2.00, t)
    detector.record(1, "home_win", 2.05, t + timedelta(minutes=1))  # 2.5% — fine
    detector.record(1, "home_win", 1.60, t + timedelta(minutes=2))  # 22% — ANOMALY
    detector.record(2, "away_win", 3.00, t)
    detector.record(2, "away_win", 2.95, t + timedelta(minutes=1))  # 1.7% — fine

    anomalies = detector.check_for_anomalies()
    test("1 anomaly detected",     len(anomalies), 1)
    test("correct match_id",       anomalies[0]["match_id"], 1)
    test("correct outcome",        anomalies[0]["outcome"], "home_win")
    test("change_pct >= 0.10",     anomalies[0]["change_pct"] >= 0.10, True)
except Exception as e:
    print(f"  ❌ ERROR: {e}")

print()
