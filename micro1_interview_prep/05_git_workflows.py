"""
Micro1 AI Interview Prep - Module 5: Git & Development Workflows
================================================================

VERBAL INTERVIEW QUESTIONS about Git and modern development practices.
"""


# ============================================
# GIT FUNDAMENTALS
# ============================================

GIT_QUESTIONS = [
    {
        "question": "Explain your typical Git workflow when working on a feature.",
        "key_points": [
            "Create feature branch from main/develop",
            "Make small, focused commits",
            "Write descriptive commit messages",
            "Push regularly (backup and visibility)",
            "Create pull request when ready",
            "Code review before merge",
            "Delete branch after merge",
        ],
        "example_answer": """
When starting a feature, I first make sure my main branch is up to date, then
create a feature branch with a descriptive name like feature/user-authentication.

I make small, focused commits as I work - each commit should be a logical unit that
could be reverted if needed. Commit messages describe what and why, not just 'fixed bug'.

I push my branch regularly to the remote - this backs up my work and lets others
see progress if needed.

When the feature is ready, I create a pull request with a clear description of what
changed and why. I address any reviewer feedback, and once approved, I merge to main.

After merging, I delete the feature branch to keep things clean.
"""
    },
    {
        "question": "What's the difference between merge and rebase? When would you use each?",
        "key_points": [
            "Merge creates a merge commit, preserves history",
            "Rebase replays commits on top, creates linear history",
            "Rebase for cleaning up local work",
            "Merge for shared branches",
            "Never rebase public/shared branches",
            "Squash merge can combine both benefits",
        ],
        "example_answer": """
Merge creates a merge commit that combines two branches. It preserves the complete
history of both branches, including when they diverged and when they joined.

Rebase takes commits from one branch and replays them on top of another. This creates
a cleaner, linear history but rewrites commits.

I use rebase for cleaning up my local work - rebasing my feature branch onto the
latest main keeps history clean. But I never rebase commits that others have pulled,
because rewriting shared history causes problems.

For pull requests, many teams use squash merge - it combines all commits into one,
giving a clean main branch history while keeping the detailed history in the PR.

The key rule: rebase local unpushed work, merge shared branches.
"""
    },
    {
        "question": "How do you handle merge conflicts?",
        "key_points": [
            "Pull latest changes regularly to minimize conflicts",
            "Understand both sides of the conflict",
            "Use tools (VS Code, Git Kraken) or manual edit",
            "Test after resolving",
            "Communicate with the other author if unsure",
            "Commit the resolution",
        ],
        "example_answer": """
First, I try to minimize conflicts by pulling latest changes regularly and keeping
feature branches short-lived.

When conflicts do occur, I look at both sides to understand what each change is
trying to accomplish. Sometimes it's obvious which to keep, sometimes both changes
are needed and I need to integrate them.

I use VS Code's merge editor which shows both versions side by side and lets me
choose or combine changes. For complex conflicts, I might discuss with whoever made
the other change to make sure I understand their intent.

After resolving, I always run tests to make sure the merged code works correctly.
Then I commit the resolution with a message noting the merge.

Good communication helps too - if I know someone is working on the same files, we
coordinate to minimize overlapping changes.
"""
    },
    {
        "question": "What makes a good commit message?",
        "key_points": [
            "Short summary line (50 chars or less)",
            "Imperative mood (Add feature, not Added feature)",
            "Body explains what and why, not how",
            "Reference ticket/issue numbers",
            "Separate subject from body with blank line",
            "Each commit should be focused",
        ],
        "example_answer": """
A good commit message has a short summary line in imperative mood - 'Add user
authentication' not 'Added user authentication'. This should be 50 characters or less.

If more context is needed, I add a body after a blank line. The body explains why
the change was made and any important context - the code shows how, the message
explains why.

I reference ticket numbers like 'Fixes #123' so there's a link between the commit
and the broader task.

Each commit should be focused on one thing. If I need a long message to explain
multiple changes, that's a sign I should split it into multiple commits.

In practice: 'Add password reset functionality (#456)' followed by a body if needed
explaining the approach or any tradeoffs made.
"""
    },
]


# ============================================
# CI/CD & DEVOPS
# ============================================

CICD_QUESTIONS = [
    {
        "question": "Explain CI/CD and how you've used it in your projects.",
        "key_points": [
            "CI - Continuous Integration: automated testing on every push",
            "CD - Continuous Deployment/Delivery: automated deployment",
            "Tools: GitHub Actions, GitLab CI, Jenkins, CircleCI",
            "Pipeline stages: build, test, lint, deploy",
            "Fast feedback is key",
            "Tests must be reliable (no flaky tests)",
        ],
        "example_answer": """
CI/CD automates the process from code commit to deployment.

Continuous Integration runs automated checks on every push - building the project,
running tests, checking code style. This catches problems early when they're easier
to fix.

Continuous Deployment takes that further by automatically deploying passing code
to staging or production.

I've used GitHub Actions to set up pipelines that run pytest tests, check code
formatting with Black, and deploy to cloud services when merging to main.

The key is fast, reliable feedback. If the pipeline is slow or tests are flaky,
developers start ignoring it. I make sure tests are fast and reliable, and failures
indicate real problems.

A typical pipeline might: install dependencies, run linting, run unit tests, run
integration tests, build a Docker image, deploy to staging.
"""
    },
    {
        "question": "How do you handle deployments? What's your deployment strategy?",
        "key_points": [
            "Automate deployments (no manual steps)",
            "Environment promotion: dev → staging → production",
            "Feature flags for controlled rollouts",
            "Blue-green or rolling deployments for zero downtime",
            "Easy rollback capability",
            "Monitoring after deployment",
        ],
        "example_answer": """
I automate deployments so they're repeatable and reliable. Manual deployments are
error-prone and slow.

Code typically moves through environments: development for testing, staging for
final verification, then production. Each promotion should be automated with
appropriate gates.

For production deployments, I use strategies that minimize risk. Blue-green
deployment runs two identical environments - deploy to the inactive one, test it,
then switch traffic. Rolling deployment gradually shifts traffic to new instances.

Feature flags allow deploying code that's not yet active, then enabling it when
ready. This separates deployment from release.

I always ensure easy rollback - if something goes wrong, we can revert quickly.
And after deployment, I monitor error rates and performance to catch issues early.
"""
    },
    {
        "question": "How do you handle environment-specific configuration?",
        "key_points": [
            "Environment variables for sensitive and varying config",
            "Separate config files per environment",
            "Never commit secrets to code",
            "Use secret management tools (Vault, AWS Secrets Manager)",
            "12-factor app principles",
            "Same code runs in all environments, only config differs",
        ],
        "example_answer": """
I follow the 12-factor app principle: configuration varies between environments,
code doesn't. The same Docker image runs in development, staging, and production,
only environment variables change.

Sensitive configuration like API keys and database credentials come from environment
variables or secret management systems - never committed to code. I use .env files
locally with .env.example committed to show what's needed.

For cloud deployments, I use secret management tools like AWS Secrets Manager or
Vault. These encrypt secrets and provide audit trails.

Non-sensitive config like API URLs or feature flags can be in environment-specific
config files, but I prefer environment variables for consistency.

This approach means: no secrets in repositories, no environment-specific code
branches, and clear documentation of what configuration each environment needs.
"""
    },
]


# ============================================
# DEVELOPMENT PRACTICES
# ============================================

DEV_PRACTICES = [
    {
        "question": "How do you approach code reviews as a reviewer?",
        "key_points": [
            "Focus on logic, security, maintainability",
            "Check tests are adequate",
            "Be constructive and educational",
            "Distinguish must-fix from nice-to-have",
            "Timely reviews (don't block progress)",
            "Ask questions rather than make demands",
        ],
        "example_answer": """
As a reviewer, I focus on the things that matter most: is the logic correct? Are
there security issues? Is this code maintainable?

I check that tests cover the changes, including edge cases. I look at error handling
and how the code integrates with existing systems.

My feedback is constructive. I explain why something might be problematic and
suggest alternatives. I ask questions to understand decisions rather than just
criticizing.

I distinguish between must-fix issues and nice-to-have suggestions. A security bug
needs fixing before merge; a slightly better variable name is optional.

I prioritize reviewing quickly - blocking a teammate's progress for days isn't
helpful. Even a quick first pass with major concerns is better than a perfect
review in a week.
"""
    },
    {
        "question": "Tell me about your experience with Agile/Scrum practices.",
        "key_points": [
            "Sprint planning and estimation",
            "Daily standups for coordination",
            "Sprint reviews and demos",
            "Retrospectives for improvement",
            "Backlog grooming",
            "Iterative delivery",
        ],
        "example_answer": """
I've worked in Scrum teams for several years. We work in two-week sprints, starting
with planning where we commit to work for the sprint based on estimates and capacity.

Daily standups keep everyone aligned - we share what we're working on, any blockers,
and coordinate on dependent work. These are short, focused updates.

At sprint end, we demo completed work to stakeholders. This provides regular
feedback and visibility into progress.

Retrospectives are valuable - we discuss what went well, what didn't, and commit
to specific improvements. This continuous improvement adds up over time.

I appreciate Agile's iterative approach. Rather than planning everything upfront,
we deliver working software regularly and adapt based on feedback. This works well
for dynamic requirements and remote teams.
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


def show_quick_reference():
    """Show all questions."""
    print("\n" + "=" * 60)
    print("QUICK REFERENCE - GIT & WORKFLOWS QUESTIONS")
    print("=" * 60)

    print("\nGIT:")
    for i, q in enumerate(GIT_QUESTIONS, 1):
        print(f"  {i}. {q['question']}")

    print("\nCI/CD:")
    for i, q in enumerate(CICD_QUESTIONS, 1):
        print(f"  {i}. {q['question']}")

    print("\nDEVELOPMENT PRACTICES:")
    for i, q in enumerate(DEV_PRACTICES, 1):
        print(f"  {i}. {q['question']}")


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("GIT & DEVELOPMENT WORKFLOWS INTERVIEW PREP")
    print("=" * 60)
    print("""
Choose an option:
1. Git Questions
2. CI/CD Questions
3. Development Practices
4. All questions
5. Quick reference (list all)
""")

    choice = input("Enter choice (1-5): ").strip()

    if choice == "1":
        run_practice(GIT_QUESTIONS, "GIT")
    elif choice == "2":
        run_practice(CICD_QUESTIONS, "CI/CD")
    elif choice == "3":
        run_practice(DEV_PRACTICES, "DEVELOPMENT PRACTICES")
    elif choice == "4":
        all_q = GIT_QUESTIONS + CICD_QUESTIONS + DEV_PRACTICES
        run_practice(all_q, "ALL GIT & WORKFLOWS")
    else:
        show_quick_reference()
