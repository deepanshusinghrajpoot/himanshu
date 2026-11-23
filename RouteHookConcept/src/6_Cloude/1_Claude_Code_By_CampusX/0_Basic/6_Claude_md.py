"""

CLAUDE.md
=========


Why CLAUDE.md?
--------------

1. LLMs do not automatically remember every detail across sessions.

2. A new Claude Code session may not have the full conversation
   history from a previous session.

3. Developers often need to repeat project instructions.

4. Repeating the same instructions is time-consuming and
   error-prone.

5. Without consistent instructions, code generation may become
   inconsistent with project conventions.

Solution:
    Store important project instructions in CLAUDE.md so Claude
    Code can refer to them while working on the project.


What Is CLAUDE.md?
------------------

Definition:
    CLAUDE.md is a Markdown instruction file used by Claude Code
    to understand project requirements, coding conventions,
    architecture, and development workflows.

    Think of it as a persistent instruction guide for your project.

Instead of repeatedly telling Claude:

    - How the project is structured
    - Which coding conventions to follow
    - How to run, build, and test the application
    - Which libraries and tools to use
    - Which files or operations to avoid

    We document these instructions in CLAUDE.md.

Important:
    Claude Code can load applicable CLAUDE.md files into its
    context. Instructions are guidance, not a guarantee that
    every rule will always be followed.


How to Create CLAUDE.md
-----------------------

There are two common methods:

1. Create It Manually

    Create a file named CLAUDE.md in the project root.

    Example:

        my-project/
        |
        |---- CLAUDE.md
        |---- package.json
        |---- src/
        |---- tests/

    Add the project's instructions using Markdown.

2. Use /init

    Open Claude Code in the project directory and run:

        /init

    Claude Code analyzes the project and helps create or update
    a CLAUDE.md file.

    Review the generated content and correct anything inaccurate.


Why Use /init?
--------------

Situation                              Why /init Helps
---------                              ---------------
Existing codebase                     Helps identify project patterns
Large repository                      Helps summarize project structure
New to CLAUDE.md                      Provides a starting point
Quick prototype                       Reduces initial documentation effort

Remember:
    /init is a starting point, not a replacement for reviewing
    the codebase and documenting important project-specific rules.


How Does /init Work?
--------------------

Typical workflow:

    1. Start Claude Code in your project directory.

    2. Run /init.

    3. Claude examines relevant project files and structure.

    4. It identifies the technology stack, scripts, conventions,
       and other useful project information.

    5. It creates or updates CLAUDE.md with the findings.

    6. Review the file and correct inaccurate or missing details.

Files Claude may inspect include:

    - README.md
    - package.json
    - requirements.txt
    - pyproject.toml
    - Makefile
    - Existing source files and configuration files

Important:
    The exact inspection process depends on the repository.

    Do not assume a fixed percentage of generated instructions
    will be useful. The result depends on project complexity
    and the quality of existing documentation.

    You should add missing workflows, constraints, security
    requirements, testing instructions, and deployment details.


Content of CLAUDE.md
====================


1. Project Context
------------------

Purpose:
    Explain what the project does and what problem it solves.

Example:

    This is a FastAPI backend for a health-tracking application.
    It stores patient BMI records and exposes CRUD APIs.

Remember:
    Keep the description short and accurate.


2. Architecture
---------------

Purpose:
    Explain how the codebase is organized and where different
    types of code should be placed.

Example:

    - Routes live in routers/.
    - Business logic lives in services/.
    - Request and response schemas live in schemas/.
    - Database access logic lives in repository/.

Remember:
    Document the actual architecture of your project.
    Do not describe folders that do not exist.


3. Code Style
-------------

Purpose:
    Define coding conventions that Claude should follow.

Example:

    - Use Python type hints.
    - Use Pydantic models for API validation.
    - Keep functions small and focused.
    - Use meaningful variable and function names.
    - Handle errors consistently.
    - Follow the existing project style.

Remember:
    Prefer consistent, maintainable code over unnecessary
    changes to existing conventions.


4. Preferred Libraries
----------------------

Purpose:
    Specify preferred frameworks, libraries, and dependencies.

Example:

    - Use FastAPI for API development.
    - Use Pydantic for data validation.
    - Use SQLAlchemy for ORM operations.
    - Do not add dependencies unless they are necessary.

Remember:
    Avoid introducing a new library when an existing project
    dependency already solves the problem.


5. Commands
------------

Purpose:
    Document commands for installing dependencies, running
    the application, and executing tests.

Example:

    Install dependencies:
        pip install -r requirements.txt

    Run development server:
        uvicorn main:app --reload

    Run tests:
        pytest

Remember:
    Commands must match the actual project configuration.
    For example, the application entry point may not be main:app.


6. Critical Rules
-----------------

Purpose:
    Document important constraints and mistakes Claude must avoid.

Example:

    - Do not modify database.py without checking its dependencies.
    - Patient IDs are supplied by the client.
    - Do not generate patient IDs automatically.
    - Never commit secrets, API keys, or passwords.
    - Do not change public API contracts without approval.

Remember:
    Clearly explain why a rule matters when necessary.


7. Implemented vs. Stub Routes
------------------------------

Purpose:
    Document which API routes are fully implemented and which
    are incomplete or placeholders.

Example:

    Route                  Status
    -----                  ------
    GET /patients          Implemented
    POST /patients         Implemented
    PUT /patients/{id}     Partially implemented
    DELETE /patients/{id}  Stub

Remember:
    Keep this information updated as the project changes.

    Verify the actual route implementation before marking
    a route as implemented.


The .claude Folder
==================

Definition:
    The .claude/ directory stores project-level Claude Code
    configuration and related resources.

    Depending on the setup, it can contain:

        - settings.json
        - settings.local.json
        - rules/
        - skills/
        - agents/
        - Custom commands or other supported resources

    The exact supported structure depends on the Claude Code
    version and feature being used.


Project-Level vs. User-Level Configuration
------------------------------------------

Project-Level:
    Location:
        <project-root>/.claude/

    Scope:
        Applies to a specific project.

    Shared with Team:
        Selected configuration files can be committed to Git.

    Used For:
        Project-specific settings, rules, agents, and skills.


User-Level:
    Location:
        ~/.claude/

    On Windows, this commonly resolves to:
        %USERPROFILE%\.claude\

    Scope:
        Applies to the user's Claude Code environment across
        projects, where supported.

    Shared with Team:
        Normally personal to the current machine and user.

    Used For:
        Personal preferences, reusable skills, and user settings.


Comparison
----------

    Project-Level                     User-Level
    --------------                    ----------
    .claude/                          ~/.claude/
    Project-specific                  Personal configuration
    Can be shared through Git         Usually not shared
    Team workflows and rules          Preferences across projects


Types and Locations of CLAUDE.md
================================

1. Project Root
---------------

    Location:
        ./CLAUDE.md

    Purpose:
        Stores general instructions for the current project.

    Example:

        my-project/
        |---- CLAUDE.md
        |---- src/
        |---- tests/


2. Inside the .claude Folder
----------------------------

    Location:
        ./.claude/CLAUDE.md

    Important:
        Do not assume this file is equivalent to the root
        CLAUDE.md in every Claude Code version or setup.

        The standard project instruction file is normally
        the root-level ./CLAUDE.md. Use the documented rules
        and supported locations for the version you are using.


3. Local Personal Instructions
------------------------------

    Location:
        ./CLAUDE.local.md

    Purpose:
        Stores project-specific personal instructions that
        should not normally be shared with the team.

    Example:
        Personal preferences or local development details.

    Important:
        Verify whether the file is automatically excluded from
        Git in your setup. Add it to .gitignore if necessary.


4. Global User Instructions
---------------------------

    Location:
        ~/.claude/CLAUDE.md

    Purpose:
        Stores personal instructions that can apply across
        multiple projects.

    Example:
        - Prefer simple, readable code.
        - Explain important changes before editing files.
        - Run relevant tests after making changes.

    Remember:
        Avoid putting project-specific requirements here.


5. Subdirectory Instructions
----------------------------

    Example:

        my-project/
        |
        |---- CLAUDE.md
        |
        |---- src/
        |    |---- CLAUDE.md
        |    |---- services/
        |         |---- CLAUDE.md
        |
        |---- tests/

    Purpose:
        Provides additional instructions for particular parts
        of a repository.

    Example:
        src/CLAUDE.md can describe rules for source code.

        tests/CLAUDE.md can describe testing conventions.

    Important:
        Claude Code discovers and applies instruction files
        according to its directory and memory-loading rules.
        Do not assume every nested file is loaded in every context.


Good Practices
==============

1. Start with /init, Then Review

    Generate a starting point and remove inaccurate,
    duplicated, or unnecessary instructions.


2. Commit Shared Instructions to Git

    Keep useful project instructions version-controlled so
    the team can follow consistent conventions.


3. Include Relevant Instructions Only

    Ask:
        Would removing this instruction cause Claude to make
        a meaningful mistake?

    If not, consider removing it.


4. Use Emphasis Carefully

    Highlight critical rules only.

    If every instruction is marked as critical, the important
    instructions become harder to identify.


5. Keep Instructions Concise

    Prefer short, specific, actionable rules.

    There is no universal 200-line limit, but very long files
    can make important instructions harder to follow.


6. Split Instructions into Rules Files

    Example structure:

        .claude/
        |
        |---- rules/
        |    |---- code-style.md
        |    |---- testing.md
        |    |---- security.md
        |    |---- api-conventions.md
        |
        |---- settings.json

    Purpose:
        Separate instructions by topic to make them easier
        to maintain.

    Remember:
        Follow the supported format for path-specific rules
        in your installed Claude Code version.


7. Use @ Imports for Existing Documentation

    Example inside CLAUDE.md:

        ## API Conventions
        See @docs/api-guidelines.md

        ## Git Workflow
        See @docs/contributing.md

    Purpose:
        Reference additional documentation rather than copying
        large sections into CLAUDE.md.

    Important:
        Use supported file-import syntax when you want Claude
        to include the referenced file's contents as context.
        A plain text reference alone may not import the file.


8. Use Subdirectory Instructions When Helpful

    Add instructions close to the code they describe when
    different parts of a large repository need different rules.


9. Treat CLAUDE.md as a Living Document

    Update it as the architecture, dependencies, and workflows
    change.


10. Correct Mistakes and Record the Rule

    If Claude repeatedly makes the same project-specific mistake,
    add a clear instruction to prevent it from happening again.


11. Audit Instructions Periodically

    Remove outdated commands, old dependencies, and rules that
    no longer match the actual codebase.


Auto Memory
===========

Definition:
    Auto memory is a feature that can save useful observations
    from Claude Code sessions for use in future sessions.

Purpose:
    Help Claude retain useful project-related discoveries
    without requiring you to repeat every detail manually.

Example:
    Claude discovers that the project uses a specific database
    naming convention and records that information in memory.

    In a later session, relevant saved memory may help Claude
    follow the same convention.


Auto Memory Location
--------------------

    Common location:

        ~/.claude/projects/<project>/memory/

    Exact project directory names and memory behavior depend
    on the Claude Code setup.

Important:
    Auto memory is separate from CLAUDE.md.

    CLAUDE.md:
        Instructions you explicitly maintain.

    Auto Memory:
        Notes Claude Code may save automatically as it works.


Memory Loading
--------------

    Claude Code may automatically load a main memory file and
    make additional memory files available when relevant.

    Do not assume a fixed limit, such as exactly 200 lines,
    applies to every version or configuration.


Command
-------

    /memory

Purpose:
    Inspect or manage Claude Code memory and its settings,
    depending on the available version and interface.

Use During Development:
    - Review saved project observations.
    - Check whether auto memory is enabled.
    - Correct outdated or inaccurate saved information.

Remember:
    Use /help to check command availability in your installation.


Quick Revision
==============

    CLAUDE.md:
        Project instruction file for Claude Code.

    /init:
        Helps create or update project instructions.

    .claude/:
        Project-level Claude Code configuration and resources.

    ~/.claude/:
        User-level Claude Code configuration and resources.

    .claude/rules/:
        Organizes instructions by topic.

    CLAUDE.local.md:
        Can hold local personal instructions when supported.

    Auto Memory:
        Stores useful observations for future sessions.

    /memory:
        Inspect or manage memory features where supported.

    Best Practice:
        Keep instructions accurate, concise, actionable,
        and updated as the project evolves.

"""