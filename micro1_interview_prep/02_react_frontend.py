"""
Micro1 AI Interview Prep - Module 2: React & Frontend
=====================================================

VERBAL INTERVIEW QUESTIONS for React and frontend development.

Remember: Answer OUT LOUD to practice speaking!
"""


# ============================================
# REACT FUNDAMENTALS
# ============================================

REACT_FUNDAMENTALS = [
    {
        "question": "Explain the difference between functional and class components in React.",
        "key_points": [
            "Functional components are plain JavaScript functions",
            "Class components extend React.Component",
            "Hooks let functional components have state and lifecycle",
            "Functional components are now preferred (simpler, less boilerplate)",
            "Class components still exist in legacy code",
            "Both can do the same things now",
        ],
        "example_answer": """
Functional components are just JavaScript functions that take props and return JSX.
Class components are ES6 classes that extend React.Component and have a render method.

Historically, class components were needed for state and lifecycle methods, but with
the introduction of Hooks in React 16.8, functional components can do everything
class components can.

Today, functional components are the standard. They're simpler, have less boilerplate,
and Hooks like useState and useEffect are easier to understand than lifecycle methods.
I use functional components exclusively in new code, though I can work with class
components in legacy codebases.
"""
    },
    {
        "question": "What are React Hooks? Name the most common ones you use.",
        "key_points": [
            "Hooks let functional components use React features",
            "useState - local component state",
            "useEffect - side effects and lifecycle",
            "useContext - consume context",
            "useRef - mutable references, DOM access",
            "useMemo/useCallback - performance optimization",
            "Custom hooks for reusable logic",
        ],
        "example_answer": """
Hooks are functions that let you use React features in functional components.

The most common ones I use are:
- useState for managing component state
- useEffect for side effects like API calls, subscriptions, or DOM updates
- useContext for accessing context without prop drilling
- useRef for references to DOM elements or mutable values that persist across renders

For performance, I use useMemo to memoize expensive calculations and useCallback
to memoize functions passed to child components.

I also write custom hooks to extract and reuse logic - for example, a useApi hook
that handles loading states, error handling, and caching for data fetching.
"""
    },
    {
        "question": "Explain the useEffect hook. What's the dependency array for?",
        "key_points": [
            "useEffect runs side effects after render",
            "Replaces componentDidMount, componentDidUpdate, componentWillUnmount",
            "Dependency array controls when effect runs",
            "Empty array = run once on mount",
            "No array = run every render",
            "Specific deps = run when those deps change",
            "Return function for cleanup",
        ],
        "example_answer": """
useEffect is for side effects - things that happen outside React's rendering, like
API calls, subscriptions, or DOM manipulation.

The dependency array tells React when to re-run the effect:
- If I pass an empty array, it runs once when the component mounts
- If I include specific values, it runs when any of those values change
- If I omit the array entirely, it runs after every render

For example, if I'm fetching user data when a userId changes, I'd put userId in
the dependency array. The effect runs on mount and whenever userId changes.

You can also return a cleanup function that runs before the next effect or when
the component unmounts - useful for unsubscribing from events or cancelling requests.
"""
    },
    {
        "question": "What is state lifting in React? When would you use it?",
        "key_points": [
            "Moving state to a common ancestor component",
            "Allows sibling components to share data",
            "Parent manages state, passes down via props",
            "Children communicate via callback functions",
            "Use when multiple components need the same data",
            "Alternative: Context or state management library for global state",
        ],
        "example_answer": """
State lifting is moving state from a child component to a parent component so that
multiple children can access and modify the same data.

For example, if I have a form with separate Input components that need to validate
together, I'd lift the form state to the parent Form component. The parent holds
the values and passes them down as props, along with onChange handlers.

This way, all inputs share the same state and the parent can coordinate validation
across all fields.

I'd use state lifting when sibling components need to share state. For deeply nested
components or truly global state, I'd consider React Context or a state management
library like Redux to avoid prop drilling through many layers.
"""
    },
    {
        "question": "How do you handle forms in React?",
        "key_points": [
            "Controlled components - React manages form state",
            "useState for form values",
            "onChange handlers update state",
            "onSubmit for form submission",
            "Validation can be inline or on submit",
            "Libraries like Formik or React Hook Form for complex forms",
        ],
        "example_answer": """
I use controlled components where React state is the source of truth for form values.

Each input has a value prop tied to state and an onChange handler that updates state.
When the form submits, I have all the current values in state ready to send to an API.

For simple forms, I use useState directly. For forms with many fields, I might use
useReducer to manage the state more cleanly.

Validation can happen on change for immediate feedback, or on blur, or on submit.
I typically show error messages next to fields and disable the submit button until
validation passes.

For complex forms with many fields, nested objects, or advanced validation, I use
React Hook Form. It's more performant and has great validation integration with
libraries like Yup or Zod.
"""
    },
    {
        "question": "What is the virtual DOM and how does React use it?",
        "key_points": [
            "Virtual DOM is a lightweight copy of the real DOM",
            "React compares virtual DOM before and after state changes",
            "Only updates what actually changed (reconciliation)",
            "Diffing algorithm determines minimal changes",
            "Batches updates for performance",
            "Keys help identify which elements changed",
        ],
        "example_answer": """
The virtual DOM is a lightweight JavaScript representation of the actual DOM.
When state changes, React creates a new virtual DOM tree and compares it to the
previous one using a diffing algorithm.

React then calculates the minimum number of changes needed and applies only those
to the real DOM. This is called reconciliation.

Direct DOM manipulation is slow, so by batching updates and only changing what's
necessary, React gets good performance even with frequent updates.

This is why keys are important in lists - they help React identify which specific
elements changed, were added, or were removed, making the diffing more efficient.
"""
    },
]


# ============================================
# REACT STATE MANAGEMENT
# ============================================

REACT_STATE_MANAGEMENT = [
    {
        "question": "When would you use Context API versus Redux or other state management?",
        "key_points": [
            "Context API - built-in, good for low-frequency updates",
            "Good for: themes, user auth, locale",
            "Redux - better for complex state, frequent updates",
            "Redux has middleware, dev tools, time-travel debugging",
            "Alternatives: Zustand, Jotai, Recoil (simpler APIs)",
            "Don't over-engineer - local state is often enough",
        ],
        "example_answer": """
Context API is built into React and great for global state that doesn't change
frequently - like the current user, theme preference, or language setting.

I'd reach for Redux or Zustand when state is more complex - lots of data, frequent
updates, or when I need features like middleware or dev tools for debugging.

Redux shines when multiple parts of the app read and write the same data, and when
I need to track state changes over time.

That said, I try not to over-engineer. Many apps work fine with just useState and
Context. I only add Redux when the complexity is actually needed. For simpler global
state needs, I like Zustand because it has a cleaner API than Redux with less boilerplate.
"""
    },
    {
        "question": "How do you fetch data in React? Walk me through your approach.",
        "key_points": [
            "useEffect for fetching on mount/when deps change",
            "useState for loading, error, and data states",
            "Handle loading states and errors",
            "Cleanup to prevent state updates on unmounted components",
            "Consider caching (React Query, SWR)",
            "Error boundaries for catching render errors",
        ],
        "example_answer": """
For data fetching, I typically use useEffect with useState to manage loading, error,
and data states.

When the component mounts, useEffect triggers the fetch. I set loading to true,
make the API call, then either set the data or an error. I also include a cleanup
function using an AbortController to cancel requests if the component unmounts.

The component shows a loading spinner while loading is true, an error message if
there's an error, and the actual content when data is available.

For production applications, I prefer using React Query or SWR instead of manual
fetching. They handle caching, refetching, and synchronization automatically, and
reduce a lot of boilerplate code.
"""
    },
]


# ============================================
# REACT PERFORMANCE & BEST PRACTICES
# ============================================

REACT_PERFORMANCE = [
    {
        "question": "How do you optimize performance in a React application?",
        "key_points": [
            "Avoid unnecessary re-renders (React.memo, useMemo, useCallback)",
            "Lazy loading with React.lazy and Suspense",
            "Code splitting",
            "Virtualization for long lists (react-window)",
            "Proper key usage in lists",
            "Profiler to identify bottlenecks",
            "Don't optimize prematurely - measure first",
        ],
        "example_answer": """
First, I'd profile the app to find actual bottlenecks rather than guessing.
React DevTools Profiler shows which components re-render and why.

Common optimizations I use:

For unnecessary re-renders, React.memo wraps components to skip re-renders if props
haven't changed. useMemo caches expensive calculations, and useCallback memoizes
functions passed as props.

For large bundles, I use code splitting with React.lazy and Suspense, so users only
download what they need.

For long lists, I use virtualization libraries like react-window that only render
visible items.

But I don't optimize prematurely - I write clear code first, then optimize based
on actual performance issues.
"""
    },
    {
        "question": "What causes unnecessary re-renders and how do you prevent them?",
        "key_points": [
            "Parent re-renders cause children to re-render",
            "Creating new objects/arrays/functions in render",
            "Context changes re-render all consumers",
            "Solutions: React.memo, useMemo, useCallback",
            "Split context into smaller pieces",
            "Move state closer to where it's used",
        ],
        "example_answer": """
Unnecessary re-renders often happen when a parent component re-renders - by default,
all children re-render too even if their props didn't change.

Common causes include:
- Passing new object or array literals as props every render
- Creating new callback functions inline
- Context changes that affect all consumers

To prevent this, I wrap child components in React.memo so they only re-render when
props actually change. I use useMemo for objects and arrays, and useCallback for
functions.

For context, I split large contexts into smaller ones so changes only affect
components that need that specific data. I also keep state as local as possible -
if only one component needs some state, it shouldn't be lifted higher than necessary.
"""
    },
]


# ============================================
# FRONTEND GENERAL
# ============================================

FRONTEND_GENERAL = [
    {
        "question": "How do you approach building a responsive UI?",
        "key_points": [
            "Mobile-first design approach",
            "CSS Flexbox and Grid for layouts",
            "Media queries for breakpoints",
            "Relative units (rem, %, vh/vw)",
            "Component libraries often handle this (Material UI, Tailwind)",
            "Test on actual devices, not just browser resize",
        ],
        "example_answer": """
I take a mobile-first approach - designing for small screens first, then enhancing
for larger screens with media queries.

For layouts, I use CSS Flexbox for one-dimensional layouts and Grid for two-dimensional.
Both handle responsive behavior well with properties like flex-wrap and auto-fit.

I use relative units like rem for typography and percentages for widths, so things
scale naturally. I define breakpoints for mobile, tablet, and desktop and adjust
layouts at each.

If I'm using a component library like Material UI or Tailwind, I leverage their
responsive utilities. Tailwind's responsive prefixes like md: and lg: make responsive
styling quick.

I always test on actual devices or device emulators, not just resizing the browser,
because touch interactions and actual screen sizes reveal different issues.
"""
    },
    {
        "question": "How do you handle API integration in a React frontend?",
        "key_points": [
            "Axios or fetch for HTTP requests",
            "Centralized API client with base URL, interceptors",
            "Handle authentication tokens",
            "Error handling and user feedback",
            "Loading states",
            "Type safety with TypeScript",
        ],
        "example_answer": """
I create a centralized API client - usually with Axios - that configures the base
URL, headers, and interceptors. The interceptor automatically attaches the auth token
to requests and handles token refresh or logout on 401 errors.

API calls are organized into service modules by feature - userService, productService,
etc. Each service exports functions that call specific endpoints.

In components, I use these services with loading and error states. Every API call
shows a loading indicator, handles errors with user-friendly messages, and provides
feedback on success.

With TypeScript, I define types for request and response data that match the backend
schemas. This catches type mismatches at compile time and makes refactoring safer.

For complex data needs, I use React Query which adds caching, background refetching,
and makes the code cleaner.
"""
    },
]


# ============================================
# PRACTICE RUNNER
# ============================================

def run_practice(questions, section_name):
    """Run through questions interactively."""
    print(f"\n{'=' * 60}")
    print(f"{section_name}")
    print("=" * 60)
    print("Instructions: Read question, answer OUT LOUD, then check key points.\n")

    for i, q in enumerate(questions, 1):
        print(f"\n{'─' * 60}")
        print(f"QUESTION {i}/{len(questions)}:")
        print(f"\n  \"{q['question']}\"")

        input("\n[Answer out loud, then press Enter to see key points...]")

        print("\nKEY POINTS TO MENTION:")
        for point in q['key_points']:
            print(f"  • {point}")

        input("\n[Press Enter to see example answer...]")

        print("\nEXAMPLE ANSWER:")
        print(q['example_answer'])

        input("\n[Press Enter for next question...]")

    print(f"\n{'=' * 60}")
    print("Section complete!")


def show_quick_reference():
    """Show all questions."""
    print("\n" + "=" * 60)
    print("QUICK REFERENCE - ALL REACT/FRONTEND QUESTIONS")
    print("=" * 60)

    print("\nREACT FUNDAMENTALS:")
    for i, q in enumerate(REACT_FUNDAMENTALS, 1):
        print(f"  {i}. {q['question']}")

    print("\nSTATE MANAGEMENT:")
    for i, q in enumerate(REACT_STATE_MANAGEMENT, 1):
        print(f"  {i}. {q['question']}")

    print("\nPERFORMANCE:")
    for i, q in enumerate(REACT_PERFORMANCE, 1):
        print(f"  {i}. {q['question']}")

    print("\nFRONTEND GENERAL:")
    for i, q in enumerate(FRONTEND_GENERAL, 1):
        print(f"  {i}. {q['question']}")


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("REACT & FRONTEND INTERVIEW PREP")
    print("=" * 60)
    print("""
Choose an option:
1. React Fundamentals
2. State Management
3. Performance
4. Frontend General
5. All questions
6. Quick reference (list all)
""")

    choice = input("Enter choice (1-6): ").strip()

    if choice == "1":
        run_practice(REACT_FUNDAMENTALS, "REACT FUNDAMENTALS")
    elif choice == "2":
        run_practice(REACT_STATE_MANAGEMENT, "STATE MANAGEMENT")
    elif choice == "3":
        run_practice(REACT_PERFORMANCE, "PERFORMANCE")
    elif choice == "4":
        run_practice(FRONTEND_GENERAL, "FRONTEND GENERAL")
    elif choice == "5":
        all_questions = REACT_FUNDAMENTALS + REACT_STATE_MANAGEMENT + REACT_PERFORMANCE + FRONTEND_GENERAL
        run_practice(all_questions, "ALL REACT/FRONTEND QUESTIONS")
    else:
        show_quick_reference()
