"""

Skills in Claude Code
=====================


1. Why Do We Need Skills?
-------------------------

Claude is a general-purpose AI model.

It can:
    - Reason and solve problems.
    - Write and explain code.
    - Generate documents and presentations.
    - Analyze data.
    - Work across different technical domains.

However, general knowledge does not always produce
consistent, high-quality results for specialized tasks.

Example: PowerPoint Presentation

Claude knows:
    - What PowerPoint is.
    - How to structure slides.
    - Which Python libraries can generate presentations.
    - How to organize presentation content.

But it may not automatically know:
    - Which fonts your company prefers.
    - How to maintain consistent slide layouts.
    - Where to place charts and tables.
    - Which colors and design guidelines to follow.
    - Your organization's presentation standards.

The same problem can occur in:

    - Frontend Development
    - Data Analysis
    - Document Generation
    - Code Review
    - Database Development
    - Software Testing


Problem with Repeated Prompts
-----------------------------

One solution is to write detailed prompts every time.

However, this creates several problems:

    1. Repeated Instructions

        You must remember and retype the same instructions
        for similar tasks.

    2. Context Window Usage

        Repeating long instructions consumes context.

    3. Resource Management

        It is difficult to organize scripts, templates,
        documentation, and other resources inside prompts.

    4. Difficult to Share and Maintain

        Individual prompts are harder to version, share,
        update, and improve consistently.

    5. Prompts Do Not Compose Easily

        Combining multiple detailed prompts into one
        workflow can become difficult.


Solution: Claude Skills
-----------------------

Skills provide reusable, task-specific instructions and resources
so Claude can follow a consistent workflow for specialized tasks.


2. What Are Skills?
-------------------

Definition:

    Skills are reusable, file-based resources that provide
    Claude with domain-specific instructions, workflows,
    examples, and supporting resources.

    They help transform a general-purpose AI assistant into
    a more specialized assistant for particular tasks.

Examples:

    - Creating Word documents.
    - Generating PowerPoint presentations.
    - Performing data analysis.
    - Building frontend applications.
    - Reviewing code.
    - Working with Excel files.

Example: PowerPoint Skill

    A presentation skill can provide instructions about:

        - Slide layout and structure.
        - Font and color selection.
        - Chart and table placement.
        - Company design guidelines.
        - Presentation validation.

    Claude can use these instructions when the skill is relevant.

Remember:

    Prompt:
        Instructions for a particular request.

    Skill:
        Reusable instructions and resources for a particular
        type of task.


3. Skill Directory Structure
----------------------------

A typical skill has the following structure:

    my-skill/
    |
    |---- SKILL.md
    |
    |---- scripts/
    |    |---- validate.py
    |    |---- generate.py
    |
    |---- references/
    |    |---- design-guidelines.md
    |    |---- xml-schema.md
    |
    |---- assets/
         |---- template.pptx
         |---- logo.png
         |---- fonts/


A. SKILL.md (Required)
----------------------

    This is the main instruction file of a skill.

    It contains:

        - YAML frontmatter
        - Skill name
        - Skill description
        - Instructions
        - Workflows
        - Examples
        - Validation steps
        - References to supporting resources


Example:

    ---
    name: pptx
    description: Create and edit professional PowerPoint
      presentations using consistent layouts and design rules.
    ---

    # PowerPoint Creation Instructions

    - Use the provided presentation template.
    - Maintain consistent fonts and colors.
    - Use readable slide layouts.
    - Validate the generated presentation.

Important:

    The name and description help Claude identify the skill
    and determine when it is relevant.

    Follow the required naming and frontmatter rules for
    your installed Claude Code version.


B. scripts/
------------

    Purpose:

        Stores executable scripts that Claude can use
        when performing a task.

    Examples:

        - validate.py
        - generate.py
        - extract_data.py

    Example use:

        A validation script can check whether a generated
        document contains the required sections.


C. references/
---------------

    Purpose:

        Stores additional documentation that Claude can
        read when required.

    Examples:

        - design-guidelines.md
        - api-conventions.md
        - xml-schema.md

    Example use:

        Claude reads design-guidelines.md when it needs
        to follow a company's presentation standards.


D. assets/
-----------

    Purpose:

        Stores files used as input or templates when
        generating output.

    Examples:

        - PowerPoint templates.
        - Word templates.
        - Company logos.
        - Images.
        - Fonts.


Remember:

    SKILL.md contains the main instructions.

    Supporting files provide additional functionality,
    reference information, or reusable assets.


4. Progressive Disclosure
-------------------------

Definition:

    Progressive Disclosure means providing information
    only when it is needed.

    Skills use this approach to avoid loading every instruction
    and supporting resource into the context at once.

Three Levels:
-------------

Level 1: Skill Description

    Claude can use the skill's name and description to identify
    when the skill may be relevant.

Level 2: SKILL.md Body

    When the skill is selected, Claude loads its main instructions.

Level 3: Supporting Resources

    Additional resources, scripts, and assets are accessed
    when the task requires them.

Example:

    User:
        Create a professional PowerPoint presentation.

    Claude:
        1. Identifies the relevant PowerPoint skill.
        2. Reads the skill instructions.
        3. Uses the presentation template if required.
        4. Reads design guidelines when needed.
        5. Generates and validates the presentation.

Important:

    Supporting resources are not necessarily loaded
    automatically. The skill instructions should tell Claude
    when and how to use them.


5. Types of Skills Based on Scope
---------------------------------

There are two common locations for skills.


A. Personal Skills
------------------

    Location:

        ~/.claude/skills/

    Scope:

        Available across the user's projects.

    Used For:

        - Personal coding preferences.
        - Reusable development workflows.
        - Personal document-generation instructions.


B. Project Skills
-----------------

    Location:

        .claude/skills/

    Scope:

        Available within the relevant project.

    Shared With Team:

        Can be shared by committing the skill files to Git.

    Used For:

        - Project-specific coding standards.
        - Team development workflows.
        - Project-specific testing instructions.
        - Reusable project operations.


Comparison:
-----------

    Personal Skills                 Project Skills
    ---------------                 --------------
    ~/.claude/skills/               .claude/skills/
    Across projects                 Current project
    Personal use                    Team/project use
    Usually not shared              Can be shared through Git


6. Ways to Create Skills
------------------------

There are three common ways to create skills.


1. Create Manually

    - Create a skill directory.
    - Create SKILL.md.
    - Add YAML frontmatter.
    - Write the task-specific instructions.
    - Add supporting resources if required.


2. Use the Skill Creator

    Claude can help create a skill using a skill-creation
    workflow or an available skill-creator resource.

    General process:

        - Explain the task the skill should handle.
        - Define when the skill should be used.
        - Create the SKILL.md file.
        - Add supporting resources.
        - Test and improve the skill.

    Important:

        Skill Creator availability depends on the installed
        skills and tools.


3. Install from Community Sources

    You can use skills shared by other developers or communities.

    Before installing:

        - Review the source.
        - Inspect SKILL.md instructions.
        - Check scripts before executing them.
        - Verify dependencies and permissions.
        - Avoid untrusted or unnecessary resources.

    Remember:

        A skill can contain executable scripts.
        Treat third-party skills as code from an external source.


7. Steps to Create a Skill
--------------------------

Step 1: Identify the Need

    Identify a repeated task that requires consistent instructions.

    Example:
        Generate professional PowerPoint presentations
        using company-specific design guidelines.


Step 2: Create the Skill Directory

    Example:

        .claude/skills/pptx/


Step 3: Create SKILL.md

    Add:
        - Name
        - Description
        - Instructions
        - Workflow
        - Examples
        - Validation steps


Step 4: Add Supporting Files

    Add resources only when required.

    Example:

        scripts/
        references/
        assets/


Step 5: Test the Skill

    Give Claude a task that should trigger the skill.

    Check:
        - Is the correct skill selected?
        - Are instructions followed?
        - Are supporting resources used correctly?
        - Is the output correct?


Step 6: Iterate and Refine

    - Correct unclear instructions.
    - Add missing examples.
    - Improve validation steps.
    - Remove unnecessary resources.
    - Test again.


8. Why Use Skills?
------------------

Problem:
    Repeatedly writing detailed prompts for specialized tasks
    is inefficient.

Solution:
    Create reusable skills containing instructions and resources.

Benefits:

    1. Reusability

        Use the same instructions across multiple tasks.

    2. Less Repetition

        Avoid rewriting the same detailed prompts.

    3. Better Context Management

        Relevant instructions and resources can be loaded
        when needed.

    4. Resource Bundling

        Keep scripts, templates, documentation, and assets
        organized with the skill.

    5. Maintainability

        Update the skill once instead of correcting
        repeated prompts.

    6. Shareability

        Share project skills with teammates through Git.

    7. Consistency

        Follow the same workflow and standards across
        similar tasks.


9. Good Practices
-----------------

    1. Give every skill a clear and meaningful name.

    2. Write a specific description explaining when to use it.

    3. Keep SKILL.md focused on the task.

    4. Use supporting files for lengthy documentation.

    5. Do not add unnecessary scripts or dependencies.

    6. Include examples of expected inputs and outputs.

    7. Add validation steps to check the final result.

    8. Test the skill with real tasks.

    9. Review third-party skills before installing them.

    10. Update skills when workflows or requirements change.


10. Quick Revision
------------------

    Skill:
        A reusable collection of task-specific instructions
        and supporting resources.

    SKILL.md:
        Required main instruction file of a skill.

    YAML Frontmatter:
        Defines skill metadata such as name and description.

    scripts/:
        Contains executable helper scripts.

    references/:
        Contains additional documentation.

    assets/:
        Contains templates, fonts, images, and other resources.

    Progressive Disclosure:
        Loads information in stages when it is needed.

    Personal Skill:
        Stored in ~/.claude/skills/.

    Project Skill:
        Stored in .claude/skills/.

    Main Benefit:
        Reuse specialized instructions and resources without
        repeatedly writing long prompts.

"""