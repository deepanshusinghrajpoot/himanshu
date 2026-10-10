"""
How to Track an Empty Directory in Git
=======================================

# Problem:
# Git does not track empty directories because Git tracks
# files and their contents, not directories themselves.

# Solution:
# Create a placeholder file inside the empty directory.
# A common convention is to use a file named .gitkeep.
# Note: .gitkeep is not a special Git command or feature;
# it is simply a commonly used placeholder filename.


# Example Directory Structure
# ============================

# my_project/
#     data/
#         .gitkeep


# Steps:
# 1. Create an empty directory.
mkdir data

# 2. Create a placeholder file inside it.
# Windows Command Prompt:
type nul > data/.gitkeep

# 3. Stage the placeholder file.
git add data/.gitkeep

# 4. Commit the change.
git commit -m "Add empty data directory"


# Important Notes
# ===============

# 1. Git tracks the directory indirectly through the committed file.
# 2. .gitkeep is a naming convention, not a special Git feature.
# 3. You can use another filename instead of .gitkeep.
# 4. If the directory later contains real files, you can remove
#    .gitkeep if it is no longer needed.


# Interview Answer
# ================

# Sir, Git does not track empty directories because it tracks
# files rather than directories themselves. To preserve an empty
# directory in the repository, we can add a placeholder file,
# commonly named .gitkeep, and commit it.
"""