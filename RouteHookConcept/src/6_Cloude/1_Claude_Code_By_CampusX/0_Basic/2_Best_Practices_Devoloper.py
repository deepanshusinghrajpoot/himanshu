"""

Best Practices for Claude Code Developers
=========================================


1. One Session = One Task
------------------------

Purpose:
    Keep each session focused on a particular feature, bug fix,
    or development task.

Use During Development:
    - Create separate sessions for unrelated tasks.
    - Keep authentication, payment integration, and bug fixing
      in separate sessions when appropriate.
    - Resume the relevant session when continuing unfinished work.

How to Start a New Session:
    1. Exit the current session:

           /exit

    2. Open the project directory in the terminal:

           cd C:\\Users\\Lenovo\\my-project

    3. Start a new session:

           claude

Example:
    Session 1 -> Implement user authentication
    Session 2 -> Integrate payment gateway
    Session 3 -> Fix database connection errors

Remember:
    Use /clear to start a fresh conversation context.
    Use a separate session when you want an independent conversation.


2. Name Your Session Immediately
--------------------------------

Purpose:
    Give each session a meaningful name so you can identify it
    easily when switching between sessions.

Command:

    /rename

Example:

    /rename User Authentication

Use During Development:
    - Identify sessions quickly.
    - Find the correct conversation when using /resume.
    - Organize work by feature or bug.

Example Session Names:

    /rename Login Feature
    /rename Database Integration
    /rename API Debugging

Remember:
    Choose short, descriptive names that explain the task.


3. Commit Frequently Within a Session
------------------------------------

Purpose:
    Save completed development milestones in Git so you can
    track changes and return to a previous version if needed.

Use During Development:
    - After completing a feature.
    - After fixing an important bug.
    - After passing relevant tests.
    - Before starting a risky refactor.

Example:

    git status
    git add .
    git commit -m "Add user authentication"

Important Points:
    - Review changes before committing.
    - Run relevant tests before committing.
    - Avoid committing passwords, API keys, or .env files.
    - A Claude Code session is not a replacement for Git commits.

Remember:
    Make small, meaningful commits after verified milestones.


4. Use /btw for Quick Questions
-------------------------------

Purpose:
    Ask a quick question related to your work without adding
    the question and answer to the main conversation history.

Command:

    /btw

Example:

    /btw What does the useEffect hook do in React?

Use During Development:
    - Ask about a small code detail.
    - Clarify a command or programming concept.
    - Get a quick explanation without interrupting the main task.

Remember:
    /btw is intended for side questions.
    Its response is not added to the main conversation history,
    so important answers should be brought into the main discussion
    if they affect your implementation.


5. Export a Session Before a Big Refactor
-----------------------------------------

Purpose:
    Preserve a readable record of the conversation before making
    major changes to an application's architecture or code.

Command:

    /export

Purpose of the Command:
    Exports the conversation so you can review or save a copy.

Use During Development:
    - Before changing the database schema.
    - Before restructuring major folders.
    - Before replacing an existing implementation.
    - When you want to preserve previous technical decisions.

Example Workflow:

    1. Review the current implementation.
    2. Export the conversation using /export.
    3. Commit the current working code in Git.
    4. Perform the refactor.
    5. Run tests and verify the application.

Important Points:
    - Exporting a conversation does not back up your source code.
    - Use Git commits or another backup method to protect code.
    - Check /help if a command behaves differently in your version.

    

    
Quick Revision
==============

    One session = One focused task.
    /rename      -> Give the session a meaningful name.
    /clear       -> Start a fresh conversation context.
    /resume      -> Return to a previous session.
    git commit   -> Save a code milestone in Git.
    /btw         -> Ask a quick side question.
    /export      -> Export the conversation.


     

"""