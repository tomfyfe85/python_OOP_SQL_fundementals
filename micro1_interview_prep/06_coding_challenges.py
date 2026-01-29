"""
Micro1 AI Interview Prep - Module 6: Coding Challenges
======================================================

PRACTICE CODING EXERCISES for the technical portion.

These are typical tasks you might be asked to complete:
- Build a simple API endpoint
- Create a React component
- Debug existing code
- Implement a feature

TIME: Usually 20-30 minutes for the coding portion.

TIPS:
- Read requirements carefully before coding
- Start with a working solution, then improve
- Talk through your thinking as you code
- Ask clarifying questions if needed
- Test your code before submitting
"""


# ============================================
# FASTAPI CODING CHALLENGES
# ============================================

FASTAPI_CHALLENGE_1 = """
CHALLENGE 1: Build a Simple TODO API
=====================================

Create a FastAPI application with the following endpoints:

1. GET /todos - Return all todos
2. POST /todos - Create a new todo
3. GET /todos/{id} - Get a specific todo
4. PUT /todos/{id} - Update a todo
5. DELETE /todos/{id} - Delete a todo

Todo structure:
{
    "id": int,
    "title": string,
    "completed": boolean
}

Requirements:
- Use Pydantic models for request/response
- Store todos in memory (list or dict)
- Return appropriate status codes
- Handle not found cases (404)

TIME: ~15 minutes
"""

FASTAPI_SOLUTION_1 = '''
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# In-memory storage
todos = {}
next_id = 1


class TodoCreate(BaseModel):
    title: str
    completed: bool = False


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None


class Todo(BaseModel):
    id: int
    title: str
    completed: bool


@app.get("/todos", response_model=list[Todo])
def get_todos():
    return list(todos.values())


@app.post("/todos", response_model=Todo, status_code=201)
def create_todo(todo: TodoCreate):
    global next_id
    new_todo = Todo(id=next_id, **todo.dict())
    todos[next_id] = new_todo
    next_id += 1
    return new_todo


@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos[todo_id]


@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo_update: TodoUpdate):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")

    existing = todos[todo_id]
    update_data = todo_update.dict(exclude_unset=True)
    updated = existing.copy(update=update_data)
    todos[todo_id] = updated
    return updated


@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    del todos[todo_id]
'''


FASTAPI_CHALLENGE_2 = """
CHALLENGE 2: User Authentication Endpoint
==========================================

Create a login endpoint that:

1. POST /login - Accept username and password
2. Validate credentials against a hardcoded user list
3. Return a JWT token on success
4. Return 401 on invalid credentials

Requirements:
- Use Pydantic for request validation
- Create a simple JWT token (can use python-jose or just base64 for demo)
- Include user info in the response
- Handle errors properly

TIME: ~15 minutes
"""

FASTAPI_SOLUTION_2 = '''
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime, timedelta
import jwt  # pip install PyJWT

app = FastAPI()

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

# Fake user database
USERS = {
    "admin": {"password": "admin123", "name": "Admin User"},
    "user": {"password": "user123", "name": "Regular User"},
}


class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user: dict


def create_token(username: str) -> str:
    expire = datetime.utcnow() + timedelta(hours=24)
    payload = {
        "sub": username,
        "exp": expire
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


@app.post("/login", response_model=LoginResponse)
def login(credentials: LoginRequest):
    # Check if user exists
    if credentials.username not in USERS:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Check password
    user = USERS[credentials.username]
    if credentials.password != user["password"]:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Create token
    token = create_token(credentials.username)

    return LoginResponse(
        access_token=token,
        token_type="bearer",
        user={"username": credentials.username, "name": user["name"]}
    )
'''


FASTAPI_CHALLENGE_3 = """
CHALLENGE 3: Data Processing Endpoint
======================================

Create an endpoint that:

1. POST /analyze - Accept a list of numbers
2. Return statistics: min, max, average, sum, count
3. Handle empty list case
4. Validate that all items are numbers

Example request:
{
    "numbers": [1, 5, 3, 9, 2]
}

Example response:
{
    "count": 5,
    "sum": 20,
    "average": 4.0,
    "min": 1,
    "max": 9
}

TIME: ~10 minutes
"""

FASTAPI_SOLUTION_3 = '''
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator
from typing import List

app = FastAPI()


class NumbersRequest(BaseModel):
    numbers: List[float]

    @validator("numbers")
    def validate_not_empty(cls, v):
        if len(v) == 0:
            raise ValueError("List cannot be empty")
        return v


class StatsResponse(BaseModel):
    count: int
    sum: float
    average: float
    min: float
    max: float


@app.post("/analyze", response_model=StatsResponse)
def analyze_numbers(data: NumbersRequest):
    numbers = data.numbers

    return StatsResponse(
        count=len(numbers),
        sum=sum(numbers),
        average=sum(numbers) / len(numbers),
        min=min(numbers),
        max=max(numbers)
    )
'''


# ============================================
# REACT CODING CHALLENGES
# ============================================

REACT_CHALLENGE_1 = """
CHALLENGE 1: Build a Counter Component
=======================================

Create a React component with:
- A number display starting at 0
- An "Increment" button that adds 1
- A "Decrement" button that subtracts 1
- A "Reset" button that sets it back to 0
- The count should not go below 0

TIME: ~10 minutes
"""

REACT_SOLUTION_1 = '''
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  const increment = () => setCount(count + 1);
  const decrement = () => setCount(Math.max(0, count - 1));
  const reset = () => setCount(0);

  return (
    <div>
      <h1>Count: {count}</h1>
      <button onClick={increment}>Increment</button>
      <button onClick={decrement}>Decrement</button>
      <button onClick={reset}>Reset</button>
    </div>
  );
}

export default Counter;
'''


REACT_CHALLENGE_2 = """
CHALLENGE 2: Build a Todo List Component
=========================================

Create a React component with:
- An input field to add new todos
- A button to add the todo
- A list displaying all todos
- Each todo has a delete button
- Each todo has a checkbox to mark complete
- Completed todos should be styled differently (strikethrough)

TIME: ~15 minutes
"""

REACT_SOLUTION_2 = '''
import React, { useState } from 'react';

function TodoList() {
  const [todos, setTodos] = useState([]);
  const [input, setInput] = useState('');

  const addTodo = () => {
    if (input.trim()) {
      setTodos([...todos, { id: Date.now(), text: input, completed: false }]);
      setInput('');
    }
  };

  const toggleTodo = (id) => {
    setTodos(todos.map(todo =>
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    ));
  };

  const deleteTodo = (id) => {
    setTodos(todos.filter(todo => todo.id !== id));
  };

  return (
    <div>
      <h1>Todo List</h1>
      <div>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && addTodo()}
          placeholder="Enter a todo"
        />
        <button onClick={addTodo}>Add</button>
      </div>
      <ul>
        {todos.map(todo => (
          <li key={todo.id}>
            <input
              type="checkbox"
              checked={todo.completed}
              onChange={() => toggleTodo(todo.id)}
            />
            <span style={{ textDecoration: todo.completed ? 'line-through' : 'none' }}>
              {todo.text}
            </span>
            <button onClick={() => deleteTodo(todo.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TodoList;
'''


REACT_CHALLENGE_3 = """
CHALLENGE 3: Fetch and Display Data
====================================

Create a React component that:
- Fetches a list of users from an API on mount
- Shows a loading state while fetching
- Displays the users in a list
- Handles errors gracefully

Use this API: https://jsonplaceholder.typicode.com/users

TIME: ~15 minutes
"""

REACT_SOLUTION_3 = '''
import React, { useState, useEffect } from 'react';

function UserList() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/users')
      .then(response => {
        if (!response.ok) throw new Error('Failed to fetch');
        return response.json();
      })
      .then(data => {
        setUsers(data);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h1>Users</h1>
      <ul>
        {users.map(user => (
          <li key={user.id}>
            <strong>{user.name}</strong> - {user.email}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default UserList;
'''


# ============================================
# DEBUGGING CHALLENGES
# ============================================

DEBUG_CHALLENGE_1 = """
CHALLENGE: Fix the Bug
=======================

The following code has bugs. Find and fix them:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: int

items = []

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return item

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return items[item_id]

@app.get("/items/search")
def search_items(name: str):
    return [i for i in items if name in i.name]
```

BUGS TO FIND:
1. Route ordering issue
2. Index out of bounds not handled
3. Missing response models
4. Price should probably be float, not int

TIME: ~10 minutes
"""

DEBUG_SOLUTION_1 = '''
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float  # Changed to float

class ItemResponse(Item):
    id: int

items = []

@app.post("/items", response_model=ItemResponse)
def create_item(item: Item):
    new_item = ItemResponse(id=len(items), **item.dict())
    items.append(new_item)
    return new_item

# MOVED search BEFORE {item_id} to fix route ordering
@app.get("/items/search", response_model=List[ItemResponse])
def search_items(name: str):
    return [i for i in items if name.lower() in i.name.lower()]

@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    if item_id < 0 or item_id >= len(items):  # Added bounds check
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]
'''


# ============================================
# PRACTICE RUNNER
# ============================================

def show_challenge(challenge, solution, name):
    """Display a coding challenge."""
    print(f"\n{'=' * 60}")
    print(name)
    print("=" * 60)
    print(challenge)

    input("\n[Try to solve it, then press Enter to see solution...]")

    print("\n" + "-" * 60)
    print("SOLUTION:")
    print("-" * 60)
    print(solution)

    input("\n[Press Enter for next challenge...]")


def run_fastapi_challenges():
    """Run FastAPI challenges."""
    show_challenge(FASTAPI_CHALLENGE_1, FASTAPI_SOLUTION_1, "FASTAPI: TODO API")
    show_challenge(FASTAPI_CHALLENGE_2, FASTAPI_SOLUTION_2, "FASTAPI: AUTHENTICATION")
    show_challenge(FASTAPI_CHALLENGE_3, FASTAPI_SOLUTION_3, "FASTAPI: DATA PROCESSING")


def run_react_challenges():
    """Run React challenges."""
    show_challenge(REACT_CHALLENGE_1, REACT_SOLUTION_1, "REACT: COUNTER")
    show_challenge(REACT_CHALLENGE_2, REACT_SOLUTION_2, "REACT: TODO LIST")
    show_challenge(REACT_CHALLENGE_3, REACT_SOLUTION_3, "REACT: DATA FETCHING")


def run_debug_challenges():
    """Run debugging challenges."""
    show_challenge(DEBUG_CHALLENGE_1, DEBUG_SOLUTION_1, "DEBUG: FIX THE BUGS")


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("CODING CHALLENGE PRACTICE")
    print("=" * 60)
    print("""
Choose challenges to practice:
1. FastAPI Challenges (3 exercises)
2. React Challenges (3 exercises)
3. Debugging Challenge
4. All challenges
5. Show tips for coding interviews
""")

    choice = input("Enter choice (1-5): ").strip()

    if choice == "1":
        run_fastapi_challenges()
    elif choice == "2":
        run_react_challenges()
    elif choice == "3":
        run_debug_challenges()
    elif choice == "4":
        run_fastapi_challenges()
        run_react_challenges()
        run_debug_challenges()
    else:
        print("""
TIPS FOR CODING CHALLENGES:

1. BEFORE CODING
   - Read the requirements carefully
   - Ask clarifying questions if anything is unclear
   - Plan your approach briefly (30 seconds)

2. WHILE CODING
   - Start with a basic working solution
   - Talk through your thinking (they can't see your thought process)
   - Use meaningful variable names
   - Handle basic error cases

3. COMMON FASTAPI PATTERNS
   - Always use Pydantic models for requests/responses
   - Use HTTPException for errors
   - Remember status codes: 200, 201, 204, 400, 401, 404, 500
   - Use response_model for type safety

4. COMMON REACT PATTERNS
   - useState for local state
   - useEffect with [] for mount-only effects
   - Handle loading and error states for data fetching
   - Use key prop in lists

5. TIME MANAGEMENT
   - Don't spend too long on edge cases initially
   - Get something working first, then improve
   - If stuck, explain what you're trying to do

6. IF YOU MAKE A MISTAKE
   - Stay calm, bugs happen
   - Debug methodically
   - Explain your debugging process

PRACTICE TIP: Time yourself! Try to complete each challenge
in the suggested time without looking at the solution.
""")

    print("\n" + "=" * 60)
    print("QUICK REFERENCE - KEY CODE SNIPPETS")
    print("=" * 60)
    print("""
FASTAPI BASICS:
---------------
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if not found:
        raise HTTPException(status_code=404, detail="Not found")
    return item


REACT BASICS:
-------------
import React, { useState, useEffect } from 'react';

function Component() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/data')
      .then(res => res.json())
      .then(data => {
        setData(data);
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Loading...</div>;
  return <div>{data}</div>;
}
""")
