"""
Git Workflow and Four Stages
=============================

When we work with Git, we commonly work with four stages:

1. Working Directory
2. Staging Area
3. Local Repository
4. Remote Repository


1. Working Directory
--------------------

# Role:
# The working directory contains our project files where we
# create new files or modify existing files.

# Example:
# We modify a Python file named main.py.
# These changes exist in the working directory.


2. Staging Area
---------------

# Role:
# The staging area contains the changes that we select for
# the next commit.

# Command:
git add main.py

# Why do we use it?
# To move the changes of a specific file into the staging area.

# To stage all changes in the current directory:
git add .

# Important:
# git add does not save a commit. It prepares selected changes
# to be included in the next commit.


3. Local Repository
-------------------

# Role:
# The local repository stores committed snapshots and their
# history on our computer.

# Command:
git commit -m "Update main.py"

# Why do we use it?
# To save the staged changes as a commit in the local repository.

# Important:
# A commit is stored locally. It is not automatically uploaded
# to GitHub or another remote repository.


4. Remote Repository
--------------------

# Role:
# The remote repository stores the project and its Git history
# on a remote server, such as GitHub.

# Push Command:
git push

# Why do we use it?
# To upload our local commits to the remote repository so that
# other team members can access the changes.

# Pull Command:
git pull

# Why do we use it?
# To fetch changes from the remote repository and integrate
# them into our current local branch.

# Important:
# git pull can create a merge commit or rebase changes,
# depending on the configuration and command options.


# Complete Git Workflow
# =====================

# Step 1: Create or modify files
# Working Directory

# Step 2: Select changes for the next commit
git add .

# Step 3: Save the staged changes locally
git commit -m "Add new features"

# Step 4: Share local commits with the team
git push

# To get and integrate changes made by the team
git pull


# Important Notes
# ===============

# 1. git init creates a new local Git repository.
# 2. git clone copies an existing remote repository to our computer.
# 3. git add stages changes.
# 4. git commit saves staged changes in the local repository.
# 5. git push sends local commits to the remote repository.
# 6. git pull fetches and integrates remote changes.
# 7. git fetch downloads remote updates without integrating
#    them into the current branch.


# Interview Answer
# =================

# Sir, Git follows a workflow involving the working directory,
# staging area, local repository, and remote repository.
# We modify files in the working directory, use git add to
# stage changes, git commit to save them locally, and git push
# to share our commits with the remote repository.
# To get the team's latest changes, we use git pull.
"""