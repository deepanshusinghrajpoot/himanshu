
"""

Vibe Coding vs. Spec-Driven Development (SDD)
=============================================


1. Vibe Coding
--------------

Definition:
    Vibe coding is a style of software development where you build
    software by interacting with an AI assistant through quick,
    conversational, and experimental prompts.

    Instead of defining every requirement upfront, you describe
    what you want and let AI generate code. You then test, review,
    and refine the result.

Main Problem:
    Less control over implementation details.

Example Prompt:
    Build me a user authentication system.

Questions AI may need answers to:
    - Which framework should be used?
    - Should authentication use JWT or sessions?
    - What are the password requirements?
    - What happens after three failed login attempts?
    - How should errors be handled?
    - How should user data be stored?

Potential Problems:
    - AI may make assumptions about requirements.
    - The generated code may not follow the project architecture.
    - Security requirements may be overlooked.
    - You may repeatedly correct and patch the generated code.
    - Changes may introduce unexpected bugs.

Remember:
    AI can generate code quickly, but speed does not guarantee
    correctness, security, or maintainability.


2. Spec-Driven Development (SDD)
--------------------------------

Definition:
    Spec-Driven Development is an approach in which software
    development is guided by a clearly defined specification.

    The specification describes what the system should do,
    its requirements, constraints, expected behavior, and
    acceptance criteria.

    AI can then use this specification to plan, implement,
    and test the software.

Main Goal:
    Reduce ambiguity and keep implementation aligned with
    clearly defined requirements.

Important:
    A specification is the reference for intended behavior.
    It should be updated when requirements change.

Core Components of a Specification
----------------------------------

1. Problem Statement
    Explain the problem the software must solve.

2. Functional Requirements
    Describe what the system must do.

3. API Contracts
    Define API endpoints, inputs, outputs, status codes,
    and request/response data structures.

4. Constraints
    Define technical limitations, security requirements,
    performance expectations, and technology choices.

5. Acceptance Criteria
    Define the conditions that must be satisfied for a feature
    to be considered complete.

Example: User Authentication Specification
------------------------------------------

Problem Statement:
    Build a secure authentication system for application users.

Functional Requirements:
    - Users can register and log in.
    - Users can log out.
    - Passwords must follow defined security rules.
    - Repeated failed login attempts must be handled safely.

API Contracts:
    POST /api/auth/register
    POST /api/auth/login
    POST /api/auth/logout

Constraints:
    - Hash passwords securely.
    - Validate user input.
    - Never expose passwords in API responses.
    - Follow the existing project architecture.

Acceptance Criteria:
    - Valid users can register and log in.
    - Invalid credentials return the expected error.
    - Passwords are never stored in plain text.
    - Automated tests cover important authentication scenarios.


3. Vibe Coding vs. SDD
----------------------

Vibe Coding:
    Prompt -> Generate Code -> Test -> Correct -> Repeat

Spec-Driven Development:
    Define Requirements -> Write Specification -> Plan
    -> Implement -> Test Against Specification -> Review

Key Difference:
    Vibe coding focuses on rapid interaction and experimentation.

    SDD focuses on implementing software against explicit,
    documented requirements.

Remember:
    These approaches are not mutually exclusive.
    You can use AI conversationally while still following SDD.


Our Spec-Driven Development Workflow
====================================

Phase 1: Understand the Task
----------------------------

    1. Read the problem statement.
    2. Identify functional requirements.
    3. Define API contracts and data structures.
    4. Identify constraints and edge cases.
    5. Write acceptance criteria.
    6. Review the specification before implementation.

Phase 2: Prepare the Git Branch
------------------------------

    Step 1: Check the current branch and working tree.

        git status
        git branch

    Step 2: Switch to the main branch.

        git switch main

    Step 3: Pull the latest changes.

        git pull origin main

    Step 4: Create a feature branch.

        git switch -c feature/user-authentication

    Important:
        Replace feature/user-authentication with a meaningful
        branch name for your task.

        If you have uncommitted changes, review them before
        switching branches or pulling updates.


Phase 3: Implement the Specification
------------------------------------

    1. Read CLAUDE.md and relevant project documentation.
    2. Ask Claude Code to inspect the existing architecture.
    3. Create an implementation plan based on the specification.
    4. Review the plan before making significant changes.
    5. Implement the feature in small, manageable steps.
    6. Follow project conventions and avoid unrelated changes.

    Example Prompt:

        Read CLAUDE.md and the feature specification.

        First, inspect the existing codebase and identify the
        files relevant to this feature.

        Create an implementation plan that follows the
        specification and existing project architecture.

        Do not modify any files until I approve the plan.


Phase 4: Test and Review
------------------------

    1. Run relevant automated tests.
    2. Check edge cases and error handling.
    3. Verify API inputs and outputs.
    4. Review security-sensitive changes.
    5. Check the Git diff for unintended modifications.

    Commands:

        git status
        git diff
        git diff --check

    Run the project's appropriate test command.

    Remember:
        Do not assume the feature is complete just because
        the AI generated the code successfully.


Phase 5: Commit and Push
-----------------------

    Step 1: Review the changes.

        git status
        git diff

    Step 2: Stage the intended files.

        git add <file-name>

    Step 3: Commit the changes.

        git commit -m "Add user authentication"

    Step 4: Push the feature branch.

        git push -u origin feature/user-authentication

    Important:
        Review staged changes before committing.
        Avoid committing secrets, environment files, or
        unrelated modifications.


Phase 6: Create and Merge a Pull Request
----------------------------------------

    1. Create a pull request on GitHub.
    2. Describe the changes and link the specification.
    3. Include test results.
    4. Request a code review.
    5. Resolve review comments.
    6. Merge the pull request after approval.

    Important:
        Follow your team's pull request and approval rules.
        Do not merge automatically if review or CI checks fail.


Phase 7: Clean Up the Branch
----------------------------

    Step 1: Switch to main.

        git switch main

    Step 2: Pull the latest merged changes.

        git pull origin main

    Step 3: Delete the local feature branch.

        git branch -d feature/user-authentication

    Step 4: Delete the remote branch if it was not
            automatically deleted after merging.

        git push origin --delete feature/user-authentication

    Important:
        Confirm the feature branch has been merged before
        deleting it.

        Remote branch deletion is unnecessary if GitHub or
        your team has already deleted it.


Complete Workflow
=================

    Understand the Problem
             |
             v
    Write the Specification
             |
             v
    Review Requirements and Acceptance Criteria
             |
             v
    Switch to Main and Pull Latest Code
             |
             v
    Create a Feature Branch
             |
             v
    Inspect Codebase and Read CLAUDE.md
             |
             v
    Plan the Implementation
             |
             v
    Implement the Feature
             |
             v
    Run Tests and Review Changes
             |
             v
    Commit Changes
             |
             v
    Push Feature Branch
             |
             v
    Create Pull Request
             |
             v
    Review, Approve, and Merge
             |
             v
    Update Main and Delete Feature Branch


Best Practices
==============

    1. Define requirements before writing significant code.

    2. Keep the specification clear, specific, and testable.

    3. Use CLAUDE.md for persistent project instructions.

    4. Ask AI to inspect the codebase before changing files.

    5. Review the implementation plan before major changes.

    6. Implement features in small, verifiable steps.

    7. Test the implementation against acceptance criteria.

    8. Review Git diffs before committing.

    9. Use feature branches and pull requests.

    10. Update the specification when requirements change.


Quick Revision
==============

    Vibe Coding:
        Generate and refine code through conversational prompts.

    SDD:
        Develop software using a clearly defined specification.

    Specification:
        Describes requirements, constraints, API contracts,
        and acceptance criteria.

    CLAUDE.md:
        Stores persistent project instructions.

    Feature Branch:
        Isolates work on a particular feature or task.

    Pull Request:
        Allows changes to be reviewed before merging.

    Acceptance Criteria:
        Define how to verify that a feature meets its requirements.

    Main Principle:
        Use AI to accelerate development, but use specifications,
        testing, code review, and Git to maintain control.

"""