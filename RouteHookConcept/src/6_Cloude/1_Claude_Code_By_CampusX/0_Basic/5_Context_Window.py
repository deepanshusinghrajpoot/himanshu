"""

Context Window
==============

Definition:
    A context window is the maximum amount of information, measured
    in tokens, that a model can process and use at one time.

    Think of it as the model's working memory.

    Context includes:
        - System instructions
        - Project instructions (CLAUDE.md)
        - Conversation history
        - Tool results (file contents, terminal output, etc.)
        - The current user message
        - The model's responses


Context Window vs. Tokens
------------------------

    Context Window:
        The maximum amount of information the model can handle
        in one context.

    Token:
        A small unit of text or other information processed by
        the model. A token can be a word, part of a word, or
        punctuation.

    Example:
        Context window = 200,000 tokens

        This does NOT mean every conversation uses 200,000 tokens.
        It means the model has a maximum context capacity of
        approximately 200,000 tokens, if that model supports it.

    Important:
        Claude Code's available context depends on the model and
        configuration being used. Check the current model's
        documentation instead of assuming every model has the
        same context window.


Context Window - Important Pointers
-----------------------------------

1. Context is shared across the conversation

    The model uses the available context to understand the current
    task and relevant previous messages.

2. Each new session starts with a fresh conversation context

    A new session does not automatically include the full
    conversation history from an older session.

    Project instructions and files can still provide context.

3. Both input and output consume tokens

    Input tokens may include:
        - Your messages
        - Previous conversation history
        - System and project instructions
        - Tool results

    Output tokens include:
        - Claude's responses
        - Tool calls and other generated content, where applicable

4. Do not assume Claude's replies use 6x more tokens

    Token usage depends on the length of your prompts, responses,
    tool results, and other context.

    Long responses and large tool outputs can consume many tokens.


5. Conversation history can increase input usage

    As a conversation grows, previous messages may remain part of
    the context sent to the model.

    The exact amount processed per request depends on how Claude
    Code manages conversation history, caching, and compaction.

    Example: Simplified cumulative conversation illustration

        Turn 1:
            New message + response       = 200 tokens
            Total conversation content   = 200 tokens

        Turn 2:
            New message + response       = 200 tokens
            Total conversation content   = 400 tokens

        Turn 3:
            New message + response       = 200 tokens
            Total conversation content   = 600 tokens

        Turn 4:
            New message + response       = 200 tokens
            Total conversation content   = 800 tokens

    Important:
        These numbers illustrate conversation growth only.
        They do NOT represent the exact tokens billed or processed
        on each turn.

        If all previous content is retained, later requests may
        process more input context than earlier requests.


6. Subagents have separate contexts

    Subagents can work on separate tasks using their own context.

    Example:
        Main agent:
            Understands the overall feature and coordinates work.

        Subagent:
            Investigates a bug or explores a specific file.

    The subagent can return a summary or findings to the main agent.
    Its entire working history does not necessarily enter the
    main conversation context.


7. Context can contain more than conversation messages

    Important sources of context usage include:

        - System instructions
        - CLAUDE.md project instructions
        - Conversation history
        - File contents and tool results
        - Skills and MCP tool information
        - Other model or application metadata

    Their exact token usage varies by project and configuration.


8. Auto-compaction helps manage context

    Claude Code can summarize older conversation context when
    the available context gets low.

    This process is called compaction.

    Compaction can reduce context usage, but some details may be
    summarized or omitted.

    Important:
        Do not assume a fixed compaction threshold, such as 75%,
        90%, or a specific number of reserved tokens. These values
        can vary by model and Claude Code version.


Command
-------

    /context

Purpose:
    Inspect context usage and understand what is consuming
    the available context in the current session.

Use During Development:
    - Check context usage during long coding sessions.
    - Identify large context contributors.
    - Decide whether to compact or start a new session.

Example:

    /context


Why the Context Window Matters
------------------------------

1. It affects how much information the model can consider at once.

2. It influences workflow decisions during long coding tasks.

3. Large tool outputs and unnecessary conversation history can
   use context that could otherwise support the current task.

4. When important details are lost during summarization or
   omitted from context, the model may misunderstand requirements.

5. Context capacity and usage are different from usage limits
   or billing limits.


What Happens When Context Usage Gets High?
------------------------------------------

Stage 1: Less Available Context

    More of the context window is occupied by conversation history,
    instructions, and tool results.

Stage 2: Automatic Compaction

    Claude Code may summarize older context to free up space.

Stage 3: Some Details May Be Lost

    A summary may not preserve every variable name, decision,
    error message, or implementation detail.

Stage 4: Start a Fresh Session When Appropriate

    For a new task, a fresh session can reduce irrelevant context.
    Provide the required project details and previous decisions
    when continuing work.


Command
-------

    /compact

Purpose:
    Summarize the conversation to reduce context usage while
    preserving important information for future work.

Use During Development:
    - Use it when a long session contains substantial old context.
    - Compact before starting another phase of a large task.
    - Include specific instructions about what information
      should be preserved.

Example:

    /compact Preserve the requirements, files changed, important
    decisions, errors encountered, and remaining tasks.

Remember:
    Compaction summarizes context; it does not undo file changes
    or replace Git commits.

    After compaction, verify important technical details if needed.


Good Practices
==============

1. One Session Per Feature

    Keep each session focused on one feature, bug fix, or task.

2. Use /compact Proactively

    Compact when context becomes large and older details are
    no longer needed in full.

3. Write Focused Prompts

    Clearly describe the task, relevant files, requirements,
    and expected result.

4. Use Subagents for Separate Tasks

    Delegate isolated investigations or code reviews when useful.

5. Keep CLAUDE.md Focused

    Store important project instructions, coding standards,
    commands, and architecture details in CLAUDE.md.

6. Avoid Unnecessary Tool Output

    Ask Claude to inspect relevant files instead of dumping
    entire directories or large files into the conversation.

7. Use Git Checkpoints

    Commit working changes at meaningful milestones so you can
    review or restore code independently of conversation context.

8. Start a New Session When the Task Changes

    A new session is useful when moving to an unrelated feature
    or when old conversation history is no longer relevant.

9. Verify Important Details

    After compaction or when resuming a task, check the actual
    project files, Git status, and test results rather than
    relying only on the conversation summary.


Quick Revision
==============

    Context Window:
        The maximum information the model can process at one time.

    Tokens:
        Units used to represent text and other information.

    /context:
        Inspect current context usage.

    /compact:
        Summarize conversation context to free up space.

    Subagent:
        A separate worker that can investigate a specific task.

    CLAUDE.md:
        A project instruction file that helps Claude understand
        the project's rules and conventions.

    Best Practice:
        Keep sessions focused, limit unnecessary tool output,
        preserve important project instructions, and use Git
        checkpoints.

"""