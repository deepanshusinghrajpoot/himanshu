"""




 Slash Commands
=================

Slash commands are shortcuts used inside Claude Code to perform
specific actions during application development.


1. /help
--------

Purpose:
    Displays help information and available commands.

Use During Development:
    - When you forget a command.
    - When you want to explore Claude Code features.
    - When you need help using a particular feature.

Example:

/help

Remember:
    Use /help whenever you are unsure about available commands.


2. /clear
---------

Purpose:
    Clears the current conversation and starts a fresh context.

Use During Development:
    - When switching to an unrelated feature.
    - When starting work on a different application.
    - When the previous conversation contains irrelevant details.

Example:

/clear

Remember:
    Clearing the conversation does not delete your project files
    or undo code changes already made.


3. /compact
-----------

Purpose:
    Summarizes the conversation to reduce context usage while
    preserving important information.

Use During Development:
    - When working on a large application for a long time.
    - When the conversation becomes lengthy.
    - When you want Claude to retain important project context
      while freeing up conversation space.

Example:

/compact

Remember:
    Use /compact when continuing a long development task.
    Review the summary if important project details are missing.


4. /resume
----------

Purpose:
    Opens a selector to resume a previous Claude Code session.

Use During Development:
    - When continuing a feature developed earlier.
    - When returning to a previous debugging task.
    - When you want to continue a conversation without explaining
      the entire task again.

Example:

/resume

Remember:
    Select the relevant session to continue the previous work.
    Resuming a session restores conversation context, not
    necessarily the exact terminal state.


5. /exit
--------

Purpose:
    Exits the current Claude Code session.

Use During Development:
    - When you finish your coding work.
    - When you want to close the current session.
    - Before switching to another terminal task.

Example:

/exit

Remember:
    Exiting Claude Code does not normally delete your saved
    session or project files.


6. /status
----------




7. Delete Session
-----------------

claude rm <session-id>

    





    

Important Development Tips
==========================

    1. Use /help to discover commands.
    2. Use /clear when starting an unrelated task.
    3. Use /compact during long development sessions.
    4. Use /resume to continue previous work.
    5. Use /exit when you finish working.

    IMPORTANT:
    Slash commands are entered inside Claude Code, not directly
    at the Windows CMD prompt.


    

    
 /logout
----------

Purpose:
    Signs out of your Claude account in Claude Code.

Use During Development:
    - When switching to another Claude account.
    - When troubleshooting authentication problems.
    - When you want to sign out from the current account.

Example:

    /logout

Remember:
    Logging out does not delete your project files or Git commits.
    You may need to authenticate again before using Claude Code.


    

 /model
---------

Purpose:
    View or change the Claude model used for your session.

Use During Development:
    - Choose a model suitable for complex coding tasks.
    - Adjust model selection based on availability and your plan.

Example:

    /model

Remember:
    Available models depend on your account and Claude Code version.


    


 Usage and Statistics
-----------------------

/usage
    Purpose:
        Shows usage information for the current session and
        current week, where supported.

    Use During Development:
        Monitor usage and plan longer coding sessions.


/extra-usage
    Purpose:
        Accesses additional usage options when available
        for your account.

    Use During Development:
        Check options if you reach your included usage limits.


/stats
    Purpose:
        Shows Claude Code usage statistics.

    Use During Development:
        Review your usage patterns and activity.


/insights
    Purpose:
        Provides insights into your Claude Code usage and
        development workflows, when available.

    Use During Development:
        Identify patterns in how you use Claude Code.


        

 Configuration
----------------

/config
    Purpose:
        Opens Claude Code configuration settings.

    Use During Development:
        Review or change supported preferences and behavior.


/theme
    Purpose:
        Changes the appearance theme of Claude Code.

    Use During Development:
        Choose a comfortable interface appearance.


/voice
    Purpose:
        Enables or manages voice-related interaction,
        where supported by your installed version.

    Use During Development:
        Use voice features when they are available and useful.


        

 Permissions
--------------

/permissions
    Purpose:
        Opens permission settings to review or manage which
        tools and actions Claude Code can use.


Permission Types:
    Allow:
        Allows a matching action without asking each time,
        subject to the applicable permission rules.

    Ask:
        Requests approval before a matching action.

    Deny:
        Blocks a matching action.


Permission Rule Locations:
--------------------------

1. User Settings
    Scope:
        Applies across projects for your user account.

    Use:
        Save permissions for commands you regularly use
        in different projects.

2. Project Settings
    Scope:
        Shared project configuration, typically stored in
        .claude/settings.json.

    Use:
        Configure permissions and other settings intended
        to be shared with the project team.

3. Local Project Settings
    Scope:
        Project-specific settings for your local environment,
        typically stored in .claude/settings.local.json.

    Use:
        Save personal project permissions without sharing
        those local preferences with the team.


Example Permission:
-------------------

    Allow: Bash(git init)

Purpose:
    Allows the matching Git initialization command according
    to the configured permission rules.

Important:
    Review the scope and pattern carefully before allowing
    a command. Avoid broad permissions for destructive actions.


How to Inspect Local Settings:
------------------------------

    Project Folder
        |
        +-- .claude/
              |
              +-- settings.json
              |
              +-- settings.local.json

Remember:
    settings.local.json is for local project settings.
    It is not the same as your global user settings file.

    Check the actual settings file before assuming which
    permissions are active.


    

 How to Find All Slash Commands
---------------------------------

Command:

    /help

Purpose:
    Displays available commands and help information.

How to Use:
    1. Start Claude Code.
    2. Type /help.
    3. Review the commands available in your installation.

Remember:
    Commands and features can vary by Claude Code version,
    account, and configuration.




 /plan
--------

Purpose:
    Enter plan mode to explore and plan a task before implementing it.

Use During Development:
    - Before developing a major feature.
    - Before changing application architecture.
    - Before modifying multiple files.

Example:

    /plan

    Then describe the feature you want to implement.

Remember:
    Planning first helps you review the approach before making
    significant code changes.


    
 /memory
----------

Purpose:
    Manage Claude Code's memory features, where available.

Use During Development:
    - Review project guidance and saved preferences.
    - Manage persistent notes that help across sessions.

Remember:
    Check /help because memory-related commands and features
    can vary by version.


    
 /doctor
----------

Purpose:
    Diagnose common Claude Code installation and configuration issues.

Use During Development:
    - When Claude Code fails to start correctly.
    - When experiencing configuration or environment problems.

Example:

    /doctor

    

 /init
--------

Purpose:
    Initialize project guidance for Claude Code, typically by
    creating a CLAUDE.md file.

Use During Development:
    - When starting work on an existing codebase.
    - When documenting architecture, coding conventions,
      setup instructions, and testing commands.

Example:

    /init

Remember:
    Review the generated CLAUDE.md and correct anything inaccurate.


    

 /diff
--------

Purpose:
    Review code changes made during your current session.

Use During Development:
    - Before accepting changes.
    - Before committing code.
    - When checking whether Claude modified unexpected files.

Example:

    /diff

Remember:
    Always review important changes and run relevant tests.


    

 /terminal-setup
------------------

Purpose:
    Configure supported terminal integration features.

Use During Development:
    - When setting up Claude Code in a supported terminal.
    - When terminal shortcuts or integration features are needed.

Remember:
    Availability depends on the terminal and Claude Code version.


Important:
    Commands can change between Claude Code versions.
    Use /help to check which commands are available in your setup.




    

    


   


**************************************************************************************************************************






2. Sessions in Claude Code
==========================

Definition:
    A session is a conversation with Claude Code that maintains
    conversation history and context while you work on an application.

    Each session has a unique session ID and can be resumed later.


Purpose:
    - Continue development without explaining the entire task again.
    - Return to previous coding or debugging conversations.
    - Review earlier implementation decisions.
    - Work on different tasks using separate sessions.


Important Points:
    - One project can have multiple sessions.
    - Claude Code saves session data locally.
    - On Windows, session data is typically stored under:

          %USERPROFILE%\\.claude\\projects\\

    - Resuming a session restores conversation context, but does not
      necessarily restore the exact terminal state or undo file changes.


      

3. Resume a Previous Session from the Terminal
===============================================

Command:

    claude -r

Purpose:
    Opens the session selector to choose a previous conversation.


Example (Windows CMD / VS Code Terminal):

    cd C:\\Users\\Lenovo\\my-project
    claude -r

How to Use:
    1. Run claude -r in the terminal.
    2. Select the required previous session.
    3. Use the available navigation controls, such as arrow keys.
    4. Press Enter to resume the selected session.


Use During Development:
    - Continue an unfinished feature.
    - Return to a previous debugging task.
    - Continue working without repeating the full project context.


Resume a Specific Session:
--------------------------

Command:

    claude -r SESSION_ID

Example:

    claude -r abc12345

Note:
    Replace abc12345 with the actual session ID.


4. Switch Between Sessions
==========================

Command (inside Claude Code):

    /resume

Purpose:
    Opens the session selector so you can choose another conversation.


Example:
    You are working on a React frontend, but you want to continue
    an earlier conversation about your Python data-analysis project.

    1. Type /resume inside Claude Code.
    2. Select the Python project session.
    3. Press Enter.
    4. Continue your previous task.


Use During Development:
    - Switch between different development tasks.
    - Return to an earlier bug or feature.
    - Keep unrelated work in separate conversations.


Important Points:
    - claude -r is used from the terminal.
    - /resume is used inside Claude Code.
    - Resuming a session does not merge conversations.
    - Open the relevant project directory when continuing project work.


Quick Revision
==============

    claude -r          -> Open the session selector from the terminal.
    claude -r ID       -> Resume a specific session by its ID.
    /resume            -> Select a previous session inside Claude Code.


    



"""














