"""





# Initialize a Git Repository
# ==========================

# Command:
git init

# Role:
# Initializes a new Git repository in the current directory.

# Why do we use it?
# To start tracking changes in our project using Git.

# What happens internally?
# 1. Git creates a hidden .git directory.
# 2. The .git directory stores repository metadata and version history.
# 3. The current directory becomes a Git working directory.

# Example:
mkdir my_project
cd my_project
git init

# Example Output:
Initialized empty Git repository in .../my_project/.git/

# Important Notes:
# 1. git init does not automatically track or commit files.
# 2. It does not upload code to GitHub.
# 3. If we run git init inside an existing Git repository,
#    Git generally reinitializes the existing repository
#    rather than creating a separate nested repository.
# 4. We use git add to stage files and git commit to save
#    a snapshot of the staged changes.

# Interview Answer:
# Sir, git init initializes a Git repository in the current
# directory by creating a .git directory, which stores the
# metadata required for version control.





Git Basic Commands
==================



# 1. Git Status
# =============

# Command:
git status

# Role:
# Shows the current state of the working directory and staging area.

# Why do we use it?
# To check which files are untracked, modified, staged,
# or ready to be committed.

# Example:
git status

# Important:
# 1. It does not modify files.
# 2. It does not stage or commit changes.
# 3. We commonly use it before git add and git commit.

# Interview Answer:
# Sir, git status shows the current state of our working
# directory and staging area, helping us identify which
# changes are staged, unstaged, or untracked.



# 2. Git Add
# ==========

# Command:
git add filename.py

# Role:
# Adds changes from a file to the staging area for the next commit.

# Why do we use it?
# To select the changes that we want to include in our next commit.

# Add a specific file:
git add main.py

# Add multiple specific files:
git add main.py data.py

# Add all changes in the current directory and its subdirectories:
git add .

# Important:
# 1. git add stages changes; it does not create a commit.
# 2. If we modify a file again after staging it, we need to
#    run git add again to stage the latest changes.
# 3. git add . stages new, modified, and deleted files within
#    the current directory scope, subject to Git's rules.

# Interview Answer:
# Sir, git add stages selected file changes so that they
# can be included in the next commit.


# 3. Git Restore
# ==============

# Command:
git restore filename.py

# Role:
# Discards unstaged changes in a file by restoring its contents
# from the index, which normally represents the staged version.

# Why do we use it?
# To discard unwanted changes made to a file in the working directory.

# Example:
git restore main.py

# Restore all unstaged changes in the current directory:
git restore .

# Restore a staged file from the last commit:
git restore --staged main.py

# Important:
# 1. git restore main.py can permanently discard unstaged
#    changes in that file.
# 2. git restore --staged main.py removes the file from staging
#    but keeps its working-directory changes.
# 3. If a file has both staged and unstaged changes, these
#    commands affect different versions of those changes.
# 4. Check git status before restoring files.

# Interview Answer:
# Sir, git restore is used to discard unstaged changes or
# restore files to a previous state. With --staged, it removes
# changes from the staging area without deleting the working
# directory modifications.



# 4. Git Commit
# =============

# Command:
git commit -m "Add new feature"

# Role:
# Saves the staged changes as a new commit in the local repository.

# Why do we use it?
# To create a recorded snapshot of selected project changes.

# Example:
git add main.py
git commit -m "Add login functionality"

# Meaning of -m:
# -m allows us to provide the commit message directly in the command.

# Good commit message examples:
git commit -m "Fix login validation"
git commit -m "Add customer data cleaning"
git commit -m "Update sales ETL pipeline"

# Important:
# 1. Only staged changes are included in the commit.
# 2. A commit is saved locally; git push is used to share
#    it with a remote repository.
# 3. A clear commit message explains what the change does.
# 4. Git may prevent a commit if required identity settings
#    or repository hooks are not satisfied.

# Interview Answer:
# Sir, git commit saves the staged changes as a snapshot
# in the local repository. The -m option lets us add a
# descriptive message to the commit.



# 5. Git Log
# ==========

# Command:
git log

# Role:
# Displays the commit history of the current branch.

# Why do we use it?
# To review previous commits, including their commit IDs,
# authors, dates, and messages.

# Show compact commit history:
git log --oneline

# Show a graph of branches and commits:
git log --oneline --graph --all

# Show a limited number of recent commits:
git log -5

# Important:
# 1. Each commit has a unique hash identifier.
# 2. git log normally shows commits reachable from HEAD.
# 3. It does not modify the repository or create new commits.
# 4. Press q to exit the log view in the terminal pager.

# Interview Answer:
# Sir, git log displays the commit history of a branch,
# including commit hashes, authors, dates, and messages.
# We can use options such as --oneline to view the history
# in a compact format.









"""