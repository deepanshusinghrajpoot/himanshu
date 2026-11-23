
"""


Step 1 (Connect Local Repo With Github)
_______________________________________

Option A : Brand-new repo on machine -> blank Github repo
.........................................................

$ git init 
(Initialise a new Git repository in the project directory)

$ git add .
(Stage all project files for the initial commit)

$ git commit -m "Initial Commit"
(Record the staged snapshot as the first commit)

$ git branch -M main 
(Rename the default branch to main)

$ git remote add origin https://github.com/arifpucit/vuln-app-cc.git
(Register the remote Github URL as the origin remote)

$ git remote -v
(Verify the remote connection - display fetch and push URLs)

$ git push -v origin main
(Push to Github and set upstram tracking. Use PATs or SSH keys for authentication)




Option B : Clone an existing Github repository
..............................................

$ git clone https://github.com/arifpucit/vuln-app-cc.git
(Download the repository and create a full local copy)

$ cd vuln-app-cc
(ENter the cloned project directory)

$ git remote -v
(Confirm the local repo is connected to the remote Github repo)




Option C : Resume work on already-cloned repo
.............................................

$ git checkout main && git pull origin main






Step 2 : Create a feature branch
________________________________

Always isolate new work - wether a bug fix or a new feature - in a dedicated

$ git checkout - bugs/sqli-fix
(create branch bugs)


Eg: bugs/sqli-fix
    feature/auth-mfa



    

Step 3 : Ctart Claude Session
_____________________________




"""