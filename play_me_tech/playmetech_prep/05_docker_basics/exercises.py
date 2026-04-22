"""
═══════════════════════════════════════════════════════════════════
 TOPIC 5: Docker — Containers, Dockerfiles & docker-compose
═══════════════════════════════════════════════════════════════════

WHY THIS MATTERS FOR PLAYMETECH:
  Docker is listed as a required skill. Trading systems need to run
  consistently across developer laptops, staging, and production.
  Containers make that possible.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 THEORY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THE CORE IDEA:
  A container is a lightweight, isolated process that bundles your
  app + its dependencies + its runtime. "Works on my machine" stops
  being an excuse because the machine IS the container.

KEY CONCEPTS:
  IMAGE    → A read-only template (like a class). Built from a Dockerfile.
  CONTAINER → A running instance of an image (like an object).
  REGISTRY → Where images live (Docker Hub, AWS ECR, GitHub GHCR).
  VOLUME   → Persistent storage mounted into a container.
  NETWORK  → How containers talk to each other.

DOCKERFILE ANATOMY:
  # Start from a base image
  FROM python:3.11-slim

  # Set working directory inside the container
  WORKDIR /app

  # Copy dependency list first (for layer caching)
  COPY requirements.txt .

  # Install dependencies
  RUN pip install --no-cache-dir -r requirements.txt

  # Copy application code
  COPY . .

  # Expose the port your app listens on (documentation only)
  EXPOSE 8000

  # Command to run when the container starts
  CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

LAYER CACHING (important!):
  Docker caches each step. If requirements.txt hasn't changed,
  the pip install step is skipped. ALWAYS copy requirements.txt
  BEFORE copying your source code.

COMMON DOCKER COMMANDS:
  docker build -t myapp:latest .       # build image from Dockerfile
  docker run -p 8000:8000 myapp        # run container, map port
  docker run -d myapp                  # run in background (detached)
  docker run -e DB_URL=... myapp       # pass env variable
  docker run -v ./data:/app/data myapp # mount local dir as volume
  docker ps                            # list running containers
  docker logs <container_id>           # view logs
  docker exec -it <id> bash            # get a shell inside container
  docker stop <container_id>           # stop container
  docker images                        # list local images

DOCKER COMPOSE:
  Orchestrates multiple containers together. Define in docker-compose.yml:

  version: "3.9"
  services:
    api:
      build: .
      ports:
        - "8000:8000"
      environment:
        - DATABASE_URL=postgresql://user:pass@db:5432/appdb
      depends_on:
        - db

    db:
      image: postgres:15
      environment:
        POSTGRES_USER: user
        POSTGRES_PASSWORD: pass
        POSTGRES_DB: appdb
      volumes:
        - postgres_data:/var/lib/postgresql/data

  volumes:
    postgres_data:

  Commands:
    docker compose up           # start everything
    docker compose up -d        # start in background
    docker compose down         # stop and remove containers
    docker compose logs api     # logs for the api service
    docker compose exec api bash  # shell inside running api container

ENVIRONMENT VARIABLES (never hardcode secrets!):
  Use a .env file:
    DATABASE_URL=postgresql://...
    SECRET_KEY=abc123

  Reference in docker-compose.yml:
    env_file:
      - .env

📚 DOCS TO READ:
  https://docs.docker.com/get-started/
  https://docs.docker.com/reference/dockerfile/
  https://docs.docker.com/compose/
  https://docs.docker.com/develop/dev-best-practices/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 EXERCISES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

These exercises are written-answer and design tasks.
Fill in the strings below. Tests validate your understanding.
"""

# ─────────────────────────────────────────────────────────────────
# EXERCISE 1 (Beginner) — Dockerfile for a FastAPI app
# ─────────────────────────────────────────────────────────────────
# Write a Dockerfile for a FastAPI app that:
#   - Uses python:3.11-slim as base
#   - Sets /app as working directory
#   - Copies and installs requirements.txt BEFORE copying source code
#   - Copies all other source files
#   - Exposes port 8000
#   - Runs: uvicorn main:app --host 0.0.0.0 --port 8000

DOCKERFILE_EX1 = """
# YOUR DOCKERFILE HERE
"""


# ─────────────────────────────────────────────────────────────────
# EXERCISE 2 (Beginner) — Docker commands
# ─────────────────────────────────────────────────────────────────
# Write the docker command that does each thing described.

# 2a. Build an image called "sports-api" with tag "v1.0" from the
#     current directory
COMMAND_2A = ""  # YOUR ANSWER

# 2b. Run the "sports-api:v1.0" image, mapping host port 8080
#     to container port 8000, with env var DATABASE_URL set to
#     "postgresql://admin:secret@db:5432/sportsdb", in detached mode
COMMAND_2B = ""  # YOUR ANSWER

# 2c. Get a bash shell inside a running container named "sports-api-1"
COMMAND_2C = ""  # YOUR ANSWER

# 2d. Show logs for a container named "data-pipeline-1",
#     following them in real-time (like tail -f)
COMMAND_2D = ""  # YOUR ANSWER


# ─────────────────────────────────────────────────────────────────
# EXERCISE 3 (Intermediate) — docker-compose.yml
# ─────────────────────────────────────────────────────────────────
# Write a docker-compose.yml for PlayMeTech's data pipeline stack:
#   - Service "pipeline": built from local Dockerfile
#       - Reads DATABASE_URL from a .env file
#       - Mounts a local ./data directory to /app/data in the container
#       - Depends on the "db" service
#   - Service "db": uses postgres:15 image
#       - Sets POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB
#       - Has a named volume "pgdata" mounted at /var/lib/postgresql/data
#       - Exposes port 5432 to host
#
# Use version "3.9" of the compose format.

DOCKER_COMPOSE_EX3 = """
# YOUR docker-compose.yml HERE
"""


# ─────────────────────────────────────────────────────────────────
# EXERCISE 4 (Intermediate) — Spot the bugs
# ─────────────────────────────────────────────────────────────────
# Each Dockerfile below has a problem. Identify what's wrong and
# write a corrected version.

BUGGY_DOCKERFILE_A = """
FROM python:3.11-slim
WORKDIR /app
COPY . .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--port", "8000"]
"""
# What's wrong with BUGGY_DOCKERFILE_A?
BUG_A_EXPLANATION = """
YOUR ANSWER HERE
"""
FIXED_DOCKERFILE_A = """
YOUR FIXED DOCKERFILE HERE
"""

BUGGY_DOCKERFILE_B = """
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "localhost", "--port", "8000"]
"""
# What's wrong with BUGGY_DOCKERFILE_B?
BUG_B_EXPLANATION = """
YOUR ANSWER HERE
"""
FIXED_DOCKERFILE_B = """
YOUR FIXED DOCKERFILE HERE
"""


# ─────────────────────────────────────────────────────────────────
# EXERCISE 5 (Hard) — Design questions
# ─────────────────────────────────────────────────────────────────
# Answer these in plain English. Think about what a tech interviewer
# would want to hear.

# 5a. PlayMeTech's data pipeline needs to run every 5 minutes to scrape
#     live odds. How would you run it with Docker?
#     (Think: cron job? Separate service? Something else?)
ANSWER_5A = """
YOUR ANSWER HERE
"""

# 5b. The pipeline container needs a secret API key to call a data provider.
#     A colleague suggests putting it in the Dockerfile as:
#       ENV API_KEY=abc123secret
#     Why is this a bad idea, and what's the right approach?
ANSWER_5B = """
YOUR ANSWER HERE
"""

# 5c. The API container crashes on startup because it can't connect to
#     the database. But the DB container is running. What are 3 possible
#     causes and how would you debug each?
ANSWER_5C = """
YOUR ANSWER HERE
"""


# ═══════════════════════════════════════════════════════════════════
#  TESTS
# ═══════════════════════════════════════════════════════════════════

def test(description, got, expected):
    status = "✅ PASS" if got == expected else f"❌ FAIL (got {got!r}, expected {expected!r})"
    print(f"  {status}  →  {description}")

def contains(haystack: str, *needles: str) -> bool:
    h = haystack.upper()
    return all(n.upper() in h for n in needles)

print("\n── Exercise 1: Dockerfile ──")
test("FROM python:3.11-slim",    contains(DOCKERFILE_EX1, "FROM python:3.11-slim"), True)
test("WORKDIR /app",             contains(DOCKERFILE_EX1, "WORKDIR /app"), True)
test("COPY requirements.txt",    contains(DOCKERFILE_EX1, "requirements.txt"), True)
test("RUN pip install",          contains(DOCKERFILE_EX1, "pip install"), True)
test("EXPOSE 8000",              contains(DOCKERFILE_EX1, "EXPOSE", "8000"), True)
test("CMD with uvicorn",         contains(DOCKERFILE_EX1, "uvicorn", "main:app"), True)
test("host 0.0.0.0",             contains(DOCKERFILE_EX1, "0.0.0.0"), True)

print("\n── Exercise 2: Docker commands ──")
test("2a: build with tag",        contains(COMMAND_2A, "docker build", "sports-api", "v1.0"), True)
test("2b: run detached (-d)",     contains(COMMAND_2B, "-d"), True)
test("2b: port mapping",          contains(COMMAND_2B, "8080:8000"), True)
test("2b: env var",               contains(COMMAND_2B, "DATABASE_URL"), True)
test("2c: exec -it bash",         contains(COMMAND_2C, "exec", "-it", "bash"), True)
test("2d: logs --follow",         contains(COMMAND_2D, "logs") and ("-f" in COMMAND_2D or "--follow" in COMMAND_2D), True)

print("\n── Exercise 3: docker-compose.yml ──")
test("version 3",                 contains(DOCKER_COMPOSE_EX3, "version"), True)
test("pipeline service",          contains(DOCKER_COMPOSE_EX3, "pipeline"), True)
test("db service postgres:15",    contains(DOCKER_COMPOSE_EX3, "postgres:15"), True)
test("depends_on",                contains(DOCKER_COMPOSE_EX3, "depends_on"), True)
test("volumes defined",           contains(DOCKER_COMPOSE_EX3, "volumes"), True)
test("env_file or DATABASE_URL",  contains(DOCKER_COMPOSE_EX3, "env_file") or contains(DOCKER_COMPOSE_EX3, "DATABASE_URL"), True)
test("./data mount",              contains(DOCKER_COMPOSE_EX3, "./data"), True)

print("\n── Exercise 4: Spot the bugs ──")
test("Bug A explained",           len(BUG_A_EXPLANATION.strip()) > 20, True)
test("Bug A fixed (reqs first)",  FIXED_DOCKERFILE_A.index("requirements.txt") < FIXED_DOCKERFILE_A.index("COPY . .") if "requirements.txt" in FIXED_DOCKERFILE_A and "COPY . ." in FIXED_DOCKERFILE_A else False, True)
test("Bug B explained",           len(BUG_B_EXPLANATION.strip()) > 20, True)
test("Bug B fixed (0.0.0.0)",    contains(FIXED_DOCKERFILE_B, "0.0.0.0"), True)

print("\n── Exercise 5: Design questions ──")
test("5a answered",               len(ANSWER_5A.strip()) > 30, True)
test("5b answered",               len(ANSWER_5B.strip()) > 30, True)
test("5c answered",               len(ANSWER_5C.strip()) > 30, True)
print("  ℹ️  Quality of design answers needs human review — no auto test for content")

print()
