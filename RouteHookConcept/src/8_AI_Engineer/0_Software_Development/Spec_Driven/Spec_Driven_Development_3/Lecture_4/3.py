"""


Step 7: Commit and Push Changes
_______________________________

! git add.

! git commit -m "fix bug"

! git push origin bugs/sqli-fix



Step 8: Open a pull request on Github
_____________________________________

- Navigate to the repository on Github.com - you will see a banner for the recently pushed branch
- Click the green "Compare & pull request" button next to the branch banner
- Set base branch to main - this is merge target
- Set compare branch to bugs/sqli-fix - this contains your changes
- Write a clear title and a detailed description explaining what changed and why
- Click "Create pull request" to formally submit your changes for team review



Step 9: Review, Merge the PR, and clean Up
___________________________________________

! git checkout main

! git pull origin main

! git branch -d bugs/sqli-fix







Step 10: Deploy the project 
___________________________




"""