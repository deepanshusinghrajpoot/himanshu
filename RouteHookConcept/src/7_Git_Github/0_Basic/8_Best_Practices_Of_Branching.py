"""

Branching Best Practices
========================


1. One Feature = One Branch
---------------------------

# Create a dedicated branch for each feature, bug fix,
# or improvement.

# Example:
git switch -c feature/login

# Benefit:
# Keeps changes isolated, organized, and easier to review.


2. Never Develop Directly on main
---------------------------------

# Keep the main branch stable.
# Develop features in separate branches and integrate changes
# through Pull Requests (PRs).

# Workflow:
# Create Branch -> Make Changes -> Commit -> Push
# -> Create PR -> Code Review -> Merge

# Benefit:
# Prevents incomplete or untested changes from directly
# affecting the main branch.


3. Delete Merged Branches
-------------------------

# Delete a feature branch after it has been successfully merged
# and is no longer required.

# Example:
git switch main
git branch -d feature/login

# Benefit:
# Keeps the branch list clean and organized.

# Note:
# This command deletes a local branch only.


4. Use Meaningful Branch Names
------------------------------

# Use clear and descriptive names that explain the purpose
# of the branch.

# Examples:
feature/user-login
fix/login-error
docs/update-readme
refactor/clean-code

# Benefit:
# Makes the purpose of each branch easy to understand.


5. Keep Branches Short-Lived
----------------------------

# Complete and merge changes as soon as reasonably possible.

# Workflow:
# Create Branch -> Make Small Changes -> Test
# -> Commit -> Push -> Create PR -> Merge

# Benefit:
# Reduces merge conflicts and makes code reviews easier.


# Interview Answer
# =================

# Sir, Git branching best practices include creating a separate
# branch for each feature or bug fix, avoiding direct development
# on the main branch, deleting merged branches, using meaningful
# branch names, and keeping branches short-lived. These practices
# improve collaboration, code quality, and maintainability.


"""