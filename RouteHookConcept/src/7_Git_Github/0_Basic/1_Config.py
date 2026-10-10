"""

# Check Git Version
# =================

# Command:
git --version

# Role:
# Displays the currently installed Git version.

# Why do we use it?
# To verify whether Git is installed and check its version.

# Example Output:
git version 2.50.0

# Note:
# The version number may differ depending on your installation.






# Configure Git Username and Email
# =================================

# Commands:
git config --global user.name "Deepanshu Singh"
git config --global user.email "deepanshusingh1197@gmail.com"


# Role:
# These commands configure the username and email address
# that Git records as the author identity for new commits.


# 1. Configure Username
# ---------------------

git config --global user.name "Deepanshu Singh"

# Role:
# Sets the Git username to "Deepanshu Singh".

# Why do we use it?
# Git uses this name in the author information of new commits.


# 2. Configure Email
# ------------------

git config --global user.email "deepanshusingh1197@gmail.com"

# Role:
# Sets the Git email address used in new commits.

# Why do we use it?
# Git records this email in commit metadata to identify the author.


# Meaning of --global
# ===================

# --global applies the configuration to all repositories
# for the current operating system user.

# Important:
# 1. These settings are saved in the user's global Git config.
# 2. A repository-specific configuration can override them.
# 3. These commands do not log us into GitHub.
# 4. The configured email should ideally be associated with
#    our GitHub account if we want commits linked to that account.


# Verify Configuration
# ====================

# Check the configured username
git config --global user.name

# Check the configured email
git config --global user.email

# Display all global Git settings
git config --global --list


# Interview Answer
# =================

# Sir, git config is used to configure Git settings.
# We use user.name and user.email to set the author identity
# recorded in our commits. The --global option applies these
# settings to all repositories for our operating system user.






"""