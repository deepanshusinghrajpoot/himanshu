
"""

Merge Conflict
==============

# Definition:
# A merge conflict occurs when Git cannot automatically combine
# changes from two branches, so we must resolve the differences
# manually or with a suitable merge tool.


# Why does a merge conflict occur?
# ================================

# 1. Two branches modify the same lines of a file differently.
# 2. One branch modifies a file while another branch deletes it.
# 3. Git cannot determine which changes should be kept automatically.


# How to resolve a merge conflict
# ================================

# Example:
# We have two branches:
# 1. master
# 2. ui
#
# Both branches modify the same line in app.py.
# When we merge ui into master, Git may report a conflict.


# Step 1: Switch to the target branch
# -----------------------------------

git switch master


# Step 2: Merge the other branch
# ------------------------------

git merge ui

# If a conflict occurs, Git reports the conflicted files.
# The merge will pause until the conflicts are resolved.


# Step 3: Check conflicted files
# ------------------------------

git status

# Role:
# Shows which files have merge conflicts and need resolution.


# Step 4: Open the conflicted file
# --------------------------------

# Git may mark the conflicting section like this:

<<<<<<< HEAD
print("Hello from master")
=======
print("Hello from ui")
>>>>>>> ui

# Meaning:
# <<<<<<< HEAD
# Contains the changes from the current branch (master).
#
# =======
# Separates the changes from the two branches.
#
# >>>>>>> ui
# Contains the changes from the branch being merged (ui).


# Step 5: Resolve the conflict manually
# -------------------------------------

# Decide which changes to keep, or combine both changes.
# Remove the conflict markers and save the file.

# Example resolved content:

print("Hello from master and ui")


# Step 6: Stage the resolved file
# -------------------------------

git add app.py

# Role:
# Marks the conflict in app.py as resolved by staging
# the edited file.


# Step 7: Complete the merge
# --------------------------

git commit -m "Resolve merge conflict"

# Role:
# Completes the merge by creating a merge commit when one
# is required. In a normal conflicted merge, this records
# the resolved result.


# Step 8: Verify the result
# -------------------------

git status
git log --oneline --graph --all

# Role:
# git status checks whether the working tree is clean.
# git log displays the commit history and branch structure.


# Important Notes
# ===============

# 1. Always inspect conflicted files before resolving them.
# 2. Do not blindly keep one side without understanding the changes.
# 3. Remove all conflict markers before staging the file.
# 4. You can use VS Code's options:
#    Accept Current Change
#    Accept Incoming Change
#    Accept Both Changes
# 5. Review the final file after choosing an option.
# 6. If you want to cancel an in-progress merge before completing it,
#    use:
git merge --abort

# 7. If the merge is completed and committed, git merge --abort
#    is no longer applicable.


# Interview Answer
# ================

# Sir, a merge conflict occurs when Git cannot automatically
# combine changes from different branches. To resolve it,
# I check the conflicted files using git status, open the files,
# decide which changes to keep, remove the conflict markers,
# stage the resolved files using git add, and complete the
# merge with git commit when required.


"""
