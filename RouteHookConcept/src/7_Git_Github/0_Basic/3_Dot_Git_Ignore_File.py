
"""




Git .gitignore File
===================

# Role:
# The .gitignore file tells Git which untracked files and
# directories it should ignore.

# Why do we use it?
# To prevent unnecessary files, temporary files, and sensitive
# configuration files from being added to the repository.

# Example:
# Create a file named .gitignore in the root directory
# of your Git repository.


# Example .gitignore File
# =======================

# Ignore Python cache files
__pycache__/
*.pyc

# Ignore environment variables and secrets
.env

# Ignore virtual environments
venv/
.venv/

# Ignore dependency folders
node_modules/

# Ignore log files
*.log

# Ignore a specific file
secret.txt

# Ignore all files inside a directory
temp/


# Important Notes
# ===============

# 1. The file name must be .gitignore.
# 2. Patterns can match individual files, file types, and directories.
# 3. Git ignores matching untracked files; it does not automatically
#    stop tracking files that were already committed.
# 4. To stop tracking a previously committed file but keep it locally:
git rm --cached filename

# 5. To stop tracking a directory but keep it locally:
git rm -r --cached directory_name

# 6. After removing tracked files from the index, commit the change.
# 7. .gitignore does not replace proper secret management.
#    Never commit passwords, API keys, or other credentials.


# Example Workflow
# =================

# 1. Create or edit the .gitignore file.
# 2. Add patterns for files and folders to ignore.
# 3. Check the repository status.
git status

# 4. Stage the .gitignore file.
git add .gitignore

# 5. Commit the changes.
git commit -m "Add gitignore rules"


# Interview Answer
# ================

# Sir, .gitignore is a file used to specify patterns for
# untracked files and directories that Git should ignore.
# It helps prevent unnecessary files, generated files, and
# sensitive configuration files from being added to a repository.
# However, it does not automatically ignore files that Git
# is already tracking.



"""