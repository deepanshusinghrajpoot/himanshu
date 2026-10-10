
"""

Branching
=========

# Definition:
# A branch is an independent line of development that allows
# us to work on features or bug fixes without directly changing
# the main development branch.


# Branching Flow Diagram
# ======================

#             master
#                |
#          Create ui branch
#                |
#             master
#                |
#                +---------- ui
#                              |
#                       Develop UI feature
#                              |
#                        Commit changes
#                              |
#             master <---------+
#                |
#           Merge ui branch
#                |
#       UI changes integrated
#                |
#          Delete ui branch


# How to show all local branches
# ------------------------------

git branch

# Role:
# Lists all local branches.
# The * symbol indicates the current branch.


# How to show local and remote branches
# -------------------------------------

git branch -a

# Role:
# Lists local branches and remote-tracking branches.


# How to create a branch
# ----------------------

git branch name_of_branch

# Example:
git branch ui

# Role:
# Creates a new branch named ui.
# It does not automatically switch to that branch.


# How to switch branch
# --------------------

git switch name_of_branch

# Example:
git switch ui

# Role:
# Switches to the specified branch.


# How to create and switch to a branch
# ------------------------------------

git switch -c ui

# Role:
# Creates a new branch named ui and switches to it.
# Here, -c means create a new branch.


# How to merge ui branch into master
# ----------------------------------

# Step 1: Switch to the target branch
git switch master

# Step 2: Check the current branch
git branch

# Step 3: Merge ui into master
git merge ui

# Role:
# Merges the changes from ui into the current branch (master).

# Important:
# 1. Switch to the branch that should receive the changes
#    before running git merge.
# 2. Commit the required changes on ui before merging.
# 3. Some merges may open an editor for the commit message.
# 4. If Vim opens, press Esc, type :wq, and press Enter
#    to save and exit.
# 5. The default branch may be named main instead of master.


# How to delete a branch
# ----------------------

git branch -d ui

# Role:
# Deletes the local ui branch if Git considers it safely merged.

# Force delete a branch
git branch -D ui

# Role:
# Force-deletes the local branch even if it has unmerged changes.

# Important:
# Switch to another branch before deleting ui.
# These commands delete local branches, not remote branches.


# Complete Practical Workflow
# ===========================

# Step 1: Create and switch to the ui branch
git switch -c ui

# Step 2: Make changes to project files

# Step 3: Stage changes
git add .

# Step 4: Commit changes
git commit -m "Add UI feature"

# Step 5: Switch to master
git switch master

# Step 6: Merge ui into master
git merge ui

# Step 7: Delete ui after successful merging
git branch -d ui

# Step 8: Verify branches
git branch


# Interview Answer
# ================

# Sir, branching in Git allows us to develop features
# independently without directly affecting the main branch.
# We use git branch to list or create branches, git switch
# to switch between branches, and git merge to integrate
# changes into the current branch. After merging, we can
# delete the feature branch if it is no longer required.


# Quick Revision
# ==============

# git branch       -> List local branches
# git branch ui    -> Create a branch
# git switch ui    -> Switch to a branch
# git switch -c ui -> Create and switch to a branch
# git merge ui     -> Merge ui into the current branch
# git branch -d ui -> Safely delete a local branch
# git branch -D ui -> Force-delete a local branch
# git branch -a    -> List local and remote-tracking branches

"""
