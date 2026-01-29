"""
Micro1 AI Interview Prep - Module 4: Remote/Distributed Teams
=============================================================

VERBAL INTERVIEW QUESTIONS about collaboration in remote teams.

This role is FULLY REMOTE - they want to know you can communicate well!
"""


# ============================================
# REMOTE WORK COMMUNICATION
# ============================================

REMOTE_COMMUNICATION = [
    {
        "question": "How do you stay productive and focused when working remotely?",
        "key_points": [
            "Dedicated workspace (not the couch)",
            "Set regular working hours",
            "Use time blocking or pomodoro technique",
            "Minimize distractions (notifications, phone)",
            "Take proper breaks",
            "Separate work and personal life",
            "Regular exercise and stepping away from screen",
        ],
        "example_answer": """
I maintain a dedicated workspace that signals to my brain it's work time. I keep
regular hours, which helps both productivity and work-life balance.

I use time blocking - I schedule focused work periods for coding and separate time
for meetings and communication. During focus time, I close Slack and email.

I take proper breaks - stepping away from the screen, getting fresh air. This
actually improves my productivity because I come back refreshed.

I also set clear boundaries between work and personal life. When I finish for the
day, I close my laptop and don't check messages until the next day, unless something
is urgent.
"""
    },
    {
        "question": "How do you communicate effectively with remote team members?",
        "key_points": [
            "Over-communicate rather than under-communicate",
            "Write clearly and provide context",
            "Choose the right medium (chat vs call vs doc)",
            "Be mindful of time zones",
            "Use async communication when possible",
            "Respond in reasonable time",
            "Be explicit about availability and blockers",
        ],
        "example_answer": """
In remote work, I over-communicate rather than under-communicate. When there's no
body language or hallway chats, I make sure my updates are clear and frequent.

I choose the right medium: quick questions go in Slack, complex discussions happen
on video calls, and important decisions get documented in writing.

I'm mindful of time zones - I try to overlap with teammates for synchronous work
and use async communication for everything else. I write detailed messages with
context so people can respond without needing a back-and-forth.

I'm explicit about my availability and any blockers. If I'm stuck waiting on
something, I mention it in standup rather than quietly waiting.

I also make sure to respond to messages within a reasonable time and let people
know if I'll be away or unavailable.
"""
    },
    {
        "question": "Tell me about a time you had a miscommunication in a remote team. How did you handle it?",
        "key_points": [
            "Use STAR format (Situation, Task, Action, Result)",
            "Be honest about the situation",
            "Show what you learned",
            "Emphasize resolution and prevention",
            "Don't blame others",
        ],
        "example_answer": """
On a previous project, I was working on a feature and assumed the API format based
on our earlier discussions. The backend developer implemented something slightly
different because our requirements had evolved in a meeting I missed.

When I discovered the mismatch during integration, instead of just fixing it, I
scheduled a quick call with the backend developer. We aligned on the final design
and documented it properly.

More importantly, we improved our process. We started using shared API specs in
tools like Swagger that both frontend and backend worked from. We also made sure
meeting notes were shared with anyone who couldn't attend.

The key lesson was: never assume - verify, document, and communicate explicitly.
"""
    },
    {
        "question": "How do you build relationships with teammates you've never met in person?",
        "key_points": [
            "Regular 1-on-1 video calls (cameras on)",
            "Informal chats - not just work topics",
            "Participate in virtual team activities",
            "Be responsive and reliable",
            "Share knowledge and help others",
            "Show genuine interest in colleagues",
        ],
        "example_answer": """
Building relationships remotely requires deliberate effort. I always have my camera
on for calls - it makes conversations more personal and builds connection.

I make time for informal chat, not just task-focused communication. I ask colleagues
how they're doing, remember details about their lives, and share a bit about mine.

I participate in virtual team activities - whether that's team games, coffee chats,
or just casual Friday channels. These moments build rapport that makes work
collaboration smoother.

I also build trust through my work - being reliable, responsive, and helpful.
When I can help a teammate with something, I do. Knowledge sharing and supporting
others builds stronger working relationships than any team-building activity.
"""
    },
]


# ============================================
# COLLABORATION PROCESSES
# ============================================

COLLABORATION_PROCESSES = [
    {
        "question": "How do you handle disagreements or conflicts with remote teammates?",
        "key_points": [
            "Address issues directly but respectfully",
            "Move from text to video call",
            "Focus on the problem, not the person",
            "Listen to understand, not to respond",
            "Find common ground and compromise",
            "Escalate appropriately if needed",
        ],
        "example_answer": """
When there's a disagreement, I first make sure I understand the other person's
perspective. Often conflicts arise from misunderstanding, not fundamental disagreement.

I move the conversation to a video call rather than continuing in text - tone is
easily misread in chat. On the call, I focus on the problem, not the person. I ask
questions to understand their reasoning and explain mine.

I look for common ground. Usually we both want what's best for the project but have
different views on how to get there. Sometimes we can find a middle ground or agree
to try one approach and revisit if it doesn't work.

If we can't resolve it, I'm comfortable involving a lead or manager to help decide.
That's not about escalating conflict - it's getting another perspective to move forward.
"""
    },
    {
        "question": "How do you handle cross-functional collaboration remotely?",
        "key_points": [
            "Regular sync meetings with other teams",
            "Shared documentation and specs",
            "Clear ownership and interfaces",
            "Proactive communication of changes",
            "Joint planning for dependent work",
            "Build relationships with key contacts",
        ],
        "example_answer": """
Cross-functional collaboration remotely requires extra structure. I establish regular
sync points with teams I depend on or who depend on me - even brief weekly calls
keep everyone aligned.

I emphasize written documentation. API contracts, requirements, and decisions are
documented in shared spaces where everyone can reference them.

I'm proactive about communicating changes that might affect other teams. If I'm
changing something that impacts the frontend, I give them a heads up early, not
when I'm ready to merge.

For dependent work, I coordinate timelines and plan together. If the backend API
needs to be ready before frontend work can begin, we align on dates and communicate
blockers quickly.

Building relationships with key contacts in other teams helps - when you need to
coordinate, it's easier if you already have rapport.
"""
    },
    {
        "question": "How do you keep track of what everyone is working on in a distributed team?",
        "key_points": [
            "Daily standups (async or sync)",
            "Clear task management (Jira, Linear, etc.)",
            "Regular team updates",
            "Status visible in shared tools",
            "Demos and show-and-tell sessions",
            "Sprint reviews and retrospectives",
        ],
        "example_answer": """
We use a combination of tools and rituals. Daily standups - either quick sync calls
or async updates in Slack - share what everyone's working on and any blockers.

Our project management tool - whether that's Jira, Linear, or GitHub Projects -
shows the current status of all work. I keep my tasks updated so the team has
visibility.

Weekly team meetings provide broader updates - completed work, upcoming priorities,
and any cross-cutting concerns.

We also do regular demos where people show what they've built. This keeps everyone
aware of progress and often sparks useful feedback.

Sprint retrospectives help us improve our processes - if something isn't working
for visibility or coordination, we discuss and fix it.
"""
    },
]


# ============================================
# ASYNC & DOCUMENTATION
# ============================================

ASYNC_WORK = [
    {
        "question": "What's your approach to asynchronous communication?",
        "key_points": [
            "Write clear, contextual messages",
            "Don't expect immediate responses",
            "Set clear expectations about urgency",
            "Document decisions and rationale",
            "Use threads to organize discussions",
            "Record meetings for those who can't attend",
        ],
        "example_answer": """
Async communication is essential for distributed teams, especially across time zones.

I write messages that contain full context - not just 'can you help with X?' but
enough background that the person can respond without asking follow-up questions.
This respects their time and avoids back-and-forth delays.

I set clear expectations about urgency. Most messages don't need immediate responses.
If something is truly urgent, I say so explicitly and use appropriate channels.

I use threads in Slack to keep discussions organized. This makes it easier for
people to catch up and find relevant information later.

For decisions made in meetings, I document the outcome and rationale. If someone
wasn't there, they can read the notes rather than being out of the loop.

I also support recording meetings for teammates who can't attend due to time zones.
"""
    },
    {
        "question": "How do you document your work for a remote team?",
        "key_points": [
            "README files for projects/repos",
            "Architecture decision records (ADRs)",
            "API documentation (auto-generated where possible)",
            "Onboarding guides",
            "Meeting notes and decisions",
            "Keep docs updated as code changes",
            "Don't over-document - focus on high-value docs",
        ],
        "example_answer": """
Good documentation is crucial for remote teams where you can't just tap someone
on the shoulder.

Every repo I work on has a README with setup instructions, environment requirements,
and key information. This helps new team members and future me.

For architecture decisions, I write ADRs - Architecture Decision Records. These
capture what we decided, why, and what alternatives we considered. They're invaluable
when revisiting decisions later.

API documentation is auto-generated where possible - FastAPI does this with OpenAPI.
For anything that needs manual documentation, I keep it close to the code so it's
more likely to stay updated.

I document meeting decisions and action items in shared spaces. When the team
decides something, it's written down.

I focus on high-value documentation - setup guides, architecture, APIs - rather than
documenting every detail. Code should be self-documenting where possible.
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
    print("QUICK REFERENCE - REMOTE COLLABORATION QUESTIONS")
    print("=" * 60)

    print("\nCOMMUNICATION:")
    for i, q in enumerate(REMOTE_COMMUNICATION, 1):
        print(f"  {i}. {q['question']}")

    print("\nCOLLABORATION PROCESSES:")
    for i, q in enumerate(COLLABORATION_PROCESSES, 1):
        print(f"  {i}. {q['question']}")

    print("\nASYNC & DOCUMENTATION:")
    for i, q in enumerate(ASYNC_WORK, 1):
        print(f"  {i}. {q['question']}")


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("REMOTE COLLABORATION INTERVIEW PREP")
    print("=" * 60)
    print("""
Choose an option:
1. Remote Communication
2. Collaboration Processes
3. Async & Documentation
4. All questions
5. Quick reference (list all)
""")

    choice = input("Enter choice (1-5): ").strip()

    if choice == "1":
        run_practice(REMOTE_COMMUNICATION, "REMOTE COMMUNICATION")
    elif choice == "2":
        run_practice(COLLABORATION_PROCESSES, "COLLABORATION PROCESSES")
    elif choice == "3":
        run_practice(ASYNC_WORK, "ASYNC & DOCUMENTATION")
    elif choice == "4":
        all_q = REMOTE_COMMUNICATION + COLLABORATION_PROCESSES + ASYNC_WORK
        run_practice(all_q, "ALL REMOTE COLLABORATION")
    else:
        show_quick_reference()
