
"""

What is Stashing in Git?
========================

# Definition:
# Git stashing temporarily saves changes that have not been
# committed and cleans those changes from the working directory
# so that we can work on another task.

# Why do we use it?
# Suppose we are working on a UI feature, but suddenly we need
# to fix an urgent bug on another branch.
# Our current work is not complete, so we do not want to commit it.
# In this situation, we can use git stash to save our changes
# temporarily and switch to another task.


# How to do Stashing
# ==================

# Step 1: Check the current status
git status

# Role:
# Shows modified, staged, and untracked files in the repository.


# Step 2: Stash the changes
git stash

# Role:
# Saves changes to tracked files that are staged or unstaged
# and restores the working directory to a clean state.

# Important:
# By default, git stash does not include untracked files.


# Step 3: Check the stash list
git stash list

# Role:
# Displays all saved stashes.

# Example Output:
# stash@{0}: WIP on ui: abc1234 Add UI feature
# stash@{1}: WIP on master: def5678 Update application


# Step 4: Check the working directory
git status

# Role:
# Confirms that the stashed tracked changes are no longer
# present as working-directory modifications.


# Step 5: Work on an urgent task
# ------------------------------

# Now we can switch branches and work on another task.
git switch master

# Make the required changes, then stage and commit them.
git add .
git commit -m "Fix urgent bug"


# Step 6: Return to our previous branch
# -------------------------------------

git switch ui

# Role:
# Returns us to the branch where we were working previously.


# Step 7: Restore stashed changes
# -------------------------------

git stash pop

# Role:
# Applies the most recent stash and removes it from the stash
# list if it is applied successfully.

# Important:
# If conflicts occur, resolve them before continuing.
# If applying the stash fails because of conflicts, the stash
# is generally retained so that we can try again.


# Important Stash Commands
# ========================

# Save changes with a descriptive message
git stash push -m "Work on UI feature"

# Include untracked files in the stash
git stash -u

# Display all saved stashes
git stash list

# Apply the most recent stash without removing it
git stash apply

# Apply a specific stash without removing it
git stash apply stash@{1}

# Apply and remove the most recent stash if successful
git stash pop

# Delete a specific stash
git stash drop stash@{0}

# Delete all stashes
git stash clear


# Important Notes
# ===============

# 1. Stashing is useful when we need to switch tasks without
#    committing incomplete work.
# 2. git stash normally saves changes to tracked files, including
#    staged and unstaged modifications.
# 3. Use git stash -u to include untracked files.
# 4. git stash pop applies the stash and removes it if successful.
# 5. git stash apply applies the stash but keeps it in the list.
# 6. Stashing is temporary storage, not a permanent commit.
# 7. Stashing is different from an emergency commit:
#    a commit saves a snapshot in repository history, while
#    a stash temporarily stores unfinished work.


# Interview Answer
# ================

# Sir, Git stashing allows us to temporarily save uncommitted
# changes and clean the working directory without creating a
# commit. It is useful when we need to switch to another task
# before our current work is complete. We use git stash to save
# changes, git stash list to view saved stashes, and git stash
# pop to restore the latest stash and remove it if successful.


"""
