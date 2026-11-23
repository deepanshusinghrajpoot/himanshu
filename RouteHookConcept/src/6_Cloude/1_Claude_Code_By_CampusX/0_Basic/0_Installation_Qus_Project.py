"""




Claude Code Development Notes
=============================


1. Not Vibe Coding
==================

Definition:
    Vibe coding is an AI-assisted development approach where
    developers use natural-language prompts to generate, modify,
    and debug code.

    Professional AI-assisted development requires understanding
    the code, reviewing changes, and testing the application.

Basic Workflow:
    1. Describe the requirement in plain English.
    2. Ask Claude to analyze the existing code.
    3. Review the proposed implementation.
    4. Implement changes incrementally.
    5. Run tests and verify the result.
    6. Review and commit working changes.

Important Points:
    - AI-generated code can contain bugs and security issues.
    - Never accept code without understanding its impact.
    - Use Git to track changes and recover from mistakes.
    - Test important functionality before deployment.

Remember:
    Use AI as a development assistant, not as a replacement
    for engineering judgment.


2. Why Use Claude Code?
=======================

Claude Code is an AI coding assistant that can inspect project
files, modify code, execute supported tools, and help with
software development tasks.

Important Capabilities:
    - Code generation and debugging.
    - Understanding existing codebases.
    - Refactoring and improving code structure.
    - Explaining project architecture.
    - Running tests and assisting with error resolution.
    - Working across multiple files in a project.

Use During Development:
    Ask Claude to understand the existing implementation before
    making changes to avoid unnecessary modifications.

Example Prompt:

    Analyze this project and explain its architecture.
    Do not modify any files yet.


3. How to Install Claude Code
=============================

Steps:
    1. Open the official Claude Code documentation.
    2. Select the installation instructions for your OS.
    3. Follow the recommended installation method.
    4. Verify the installation.
    5. Authenticate when prompted.

Official Documentation:

    https://code.claude.com/docs/en/overview


Windows CMD Installation:
-------------------------

Command:

    curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd

Purpose:
    Downloads and runs the official Windows installer, then
    removes the downloaded installer script after execution.

Verify Installation:

    claude --version

Check Available Commands:

    claude --help

Important Points:
    - Use the official documentation for the latest instructions.
    - Review installation commands before executing them.
    - Complete authentication before starting a session.


4. How to Start Claude Code
===========================

Command:

    claude

Purpose:
    Starts an interactive Claude Code session in the current
    working directory.

Example (Windows CMD):

    cd C:\\Users\\Lenovo\\my-project
    claude

Use During Development:
    Open the correct project directory before starting Claude.
    This allows Claude to work with the intended codebase.

Remember:
    The current working directory matters when working on
    an existing application.


5. How to Run Bash Commands
===========================

Shortcut:

    Shift + !

Purpose:
    In supported Claude Code interactive terminals, this shortcut
    opens a Bash command-entry prompt to execute a shell command.

Example:

    !npm test

Note:
    Terminal and shell behavior can vary by operating system
    and Claude Code version. Follow the prompt displayed by
    your installed version.

Use During Development:
    - Run tests.
    - Check installed packages.
    - Inspect project files.
    - Run development commands.

Examples:

    npm list --depth=0
    npm test
    git status

Important Points:
    - Understand a command before running it.
    - Review commands that delete files or modify the system.
    - Do not expose API keys, passwords, or secrets.
    - Use the appropriate shell syntax for your terminal.


6. Best Practices for Using Shell Commands
==========================================

    1. Inspect files before modifying or deleting them.
    2. Run tests after making code changes.
    3. Use Git to review and track modifications.
    4. Avoid running unfamiliar commands blindly.
    5. Never paste secrets into prompts or terminal output.
    6. Review package installation commands before executing.
    7. Ask Claude to explain risky commands before running them.



    

    
7. Important Questions to Ask Claude
====================================

A. Understand the Project
-------------------------

Prompt:

    Explain what this project does, its main features, and
    how its major components work together.

Purpose:
    Understand the application's functionality before coding.


B. Identify the Technology Stack
--------------------------------

Prompt:

    Identify the technologies, frameworks, libraries, and
    tools used in this project. Explain their purpose.

Purpose:
    Understand the technologies already being used.


C. Understand the Project Structure
-----------------------------------

Prompt:

    Explain the project folder structure and the responsibility
    of each important file and directory.

Purpose:
    Find where to implement new features and fix bugs.


D. Check Installed Dependencies
--------------------------------

Prompt:

    Inspect the dependency files and explain the installed
    packages, their purposes, and any important dependencies.

Purpose:
    Understand project dependencies without installing or
    modifying anything unnecessarily.

Examples of dependency files:

    package.json
    requirements.txt
    pyproject.toml
    composer.json


E. Understand How to Run the Project
------------------------------------

Prompt:

    Explain how to install dependencies, configure the environment,
    start the application, and run its tests.

    Do not execute commands or modify files yet.

Purpose:
    Learn the correct development workflow before running commands.


F. Find Potential Problems
--------------------------

Prompt:

    Review the project for obvious bugs, security risks, and
    missing tests. Explain your findings without modifying files.

Purpose:
    Identify problems before starting development.


8. Recommended Workflow for a New Application
=============================================

    Step 1: Open the project directory.
    Step 2: Start Claude Code using claude.
    Step 3: Ask Claude to explain the project.
    Step 4: Identify the technology stack and dependencies.
    Step 5: Understand the folder structure.
    Step 6: Learn how to run the application and tests.
    Step 7: Ask Claude to inspect relevant files before coding.
    Step 8: Implement one feature at a time.
    Step 9: Review code changes and run tests.
    Step 10: Commit verified changes using Git.


Quick Revision
==============

    claude --version  -> Verify the installed version.
    claude --help     -> View CLI usage information.
    claude            -> Start an interactive session.
    Shift + !         -> Open the shell-command prompt in
                         supported Claude Code terminals.
    git status        -> Review working-tree changes.
    npm test          -> Run tests in projects configured for npm.

Remember:
    Understand first, plan second, code third, and test before
    committing or deploying.





"""