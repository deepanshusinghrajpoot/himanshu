"""

Spec-Driven Development (SDD) with Claude Code
===============================================


1. Start a New Claude Code Session
----------------------------------

    Open the terminal in your project directory.

    Command:
        claude

    Purpose:
        Start a fresh session for the database setup task.


2. Rename the Session
---------------------

    Command:
        /rename database setup

    Purpose:
        Give the session a meaningful name so you can identify
        it easily when reviewing or resuming previous sessions.


3. Pull the Latest Code
-----------------------

    Commands:
        git status
        git switch main
        git pull origin main

    Purpose:
        Get the latest code from the remote main branch.

    Remember:
        Review uncommitted changes before switching branches
        or pulling updates.


4. Create and Switch to a Feature Branch
----------------------------------------

    Command:
        git switch -c feature/database-setup

    Purpose:
        Create a new feature branch and switch to it.

    Alternative:
        git checkout -b feature/database-setup

    Important:
        Do not add a space between the hyphen and b.

        Correct:
            git checkout -b feature/database-setup

        Incorrect:
            git checkout - b feature/database-setup


5. Create the Specification Document
------------------------------------

    Create this file manually:

        .claude/specs/01-database-setup.md

    Include:
        - Problem statement
        - Functional requirements
        - Database requirements
        - Configuration requirements
        - Error handling
        - Security constraints
        - Acceptance criteria

    Purpose:
        Define WHAT needs to be built before deciding HOW
        to implement it.


6. Review the Specification
---------------------------

    File:
        .claude/specs/01-database-setup.md

    Check:
        - Are all requirements clear?
        - Is the database technology specified?
        - Are environment variables defined?
        - Are error cases covered?
        - Are security requirements documented?
        - Are acceptance criteria testable?

    Important:
        Resolve ambiguities before implementation begins.


7. Enter Plan Mode
------------------

    Method 1:
        Press Shift + Tab twice in the interactive terminal
        to cycle to Plan Mode, if supported by your version.

    Method 2:
        Use the Plan Mode control available in your version
        of Claude Code.

    Purpose:
        Ask Claude to analyze the project and prepare an
        implementation plan before making code changes.

    Note:
        Do not assume /plan is a built-in slash command in every
        version. Use /help to check available commands.


8. Generate and Save the Implementation Plan
--------------------------------------------

    Specification:
        .claude/specs/01-database-setup.md

    Existing application:
        app.py

    Plan output:
        .claude/plans/01-database-setup.md

    Prompt:

        Read .claude/specs/01-database-setup.md.

        Inspect app.py and the relevant project files.

        Create a detailed implementation plan based on the
        specification and the existing codebase.

        Include:
            - Files to create or modify
            - Database connection approach
            - Required dependencies
            - Environment variables
            - Error handling
            - Security considerations
            - Testing strategy
            - Acceptance criteria

        Do not implement the feature yet.

        Save the plan to:
        .claude/plans/01-database-setup.md

        Identify unclear requirements instead of making
        unsupported assumptions.

    Remember:
        Verify that the plan file exists and contains the
        expected implementation steps.


9. Review and Edit the Plan
---------------------------

    Open:
        .claude/plans/01-database-setup.md

    Review:
        - Does the plan satisfy the specification?
        - Are the proposed files correct?
        - Are security requirements covered?
        - Are unnecessary dependencies avoided?
        - Are tests included?
        - Are implementation steps in the correct order?

    Action:
        Manually edit the plan if required.

    Purpose:
        Catch design mistakes before writing code.


10. Implement the Approved Plan
-------------------------------

    Prompt:

        Read the specification:
        .claude/specs/01-database-setup.md

        Read the approved implementation plan:
        .claude/plans/01-database-setup.md

        Implement the plan while following CLAUDE.md and
        the existing project conventions.

        Avoid unrelated changes.

        Run the relevant tests and report:
            - Files created or modified
            - Implementation details
            - Tests executed
            - Test results
            - Remaining issues

    Remember:
        Review important changes rather than blindly accepting
        the generated code.


11. Validate Against the Specification
--------------------------------------

    Compare the implementation with:
        .claude/specs/01-database-setup.md

    Validate:
        - Functional requirements
        - Database connection behavior
        - Configuration handling
        - Error handling
        - Security requirements
        - Acceptance criteria

    Commands:
        git status
        git diff
        git diff --check

    Also run the relevant project tests.

    Remember:
        Successful execution alone does not prove that every
        requirement has been satisfied.


12. Iterate if Required
-----------------------

    If validation fails:

        1. Identify the unmet requirement.
        2. Find the root cause.
        3. Correct the implementation.
        4. Run the relevant tests again.
        5. Validate the result against the specification.

    Repeat until the requirements are satisfied or any remaining
    limitations are documented.


13. Commit the Changes
----------------------

    Review the changes:
        git status
        git diff

    Stage the intended files:
        git add .

    Commit:
        git commit -m "Set up database connection"

    Important:
        Review staged files before committing.

        Do not commit secrets, passwords, .env files, or
        unrelated changes.

        Use a meaningful commit message that describes the work.


Planning with Claude Code
=========================

1. Model Selection
------------------

    Preferred model:
        Opus

    Use a capable model for:
        - Complex implementation planning
        - Architecture decisions
        - Multi-file changes
        - Difficult debugging

    Remember:
        Model availability depends on your account and setup.


2. Extended Thinking
--------------------

    Command:
        /config

    Purpose:
        Review available configuration options and thinking
        settings, where supported.

    Use additional reasoning for complex tasks that require
    careful analysis and planning.


3. Effort Level
---------------

    Command:
        /effort

    General guidance:

        Medium:
            Routine development and moderately complex tasks.

        High:
            Complex planning, debugging, and architecture decisions.

    Remember:
        Available effort levels depend on the model and version.


4. Ultraplan
------------

    Example:
        /ultraplan Create a database setup implementation plan
        using .claude/specs/01-database-setup.md.

    Important:
        Use /ultraplan only if your installation or configured
        extension supports it.

    Alternative:
        Use Plan Mode and ask Claude to inspect the specification,
        analyze the codebase, and save the implementation plan.


Good Practices
==============

    1. Select the appropriate model for the task.

    2. Use additional reasoning for complex implementation plans.

    3. Write the specification before implementing the feature.

    4. Review the specification and plan manually.

    5. Keep specifications and implementation plans separate.

       specs/:
           Defines WHAT the system must do.

       plans/:
           Defines HOW the system will be implemented.

    6. Implement in small, manageable steps.

    7. Test every important requirement.

    8. Review code changes before committing.

    9. Keep changes focused on the requested feature.

    10. Use Git branches and meaningful commits.


Quick Revision
==============

    Specification:
        Defines what needs to be built.

    Implementation Plan:
        Defines how the feature will be built.

    Plan Mode:
        Helps Claude analyze and plan before implementation.

    Feature Branch:
        Isolates work on a particular feature.

    Validation:
        Checks the implementation against the specification.

    Git Commit:
        Records staged changes in the repository.

    Complete Workflow:
        Understand -> Specify -> Plan -> Review -> Implement
        -> Test -> Validate -> Commit

"""