"""







How delete claude session from current project
----------------------------------------------

In Power Sell

Step 1. Set your session ID
$sessionId = "fdc164f1-8977-4a6e-86e8-c982bb431fe1"


Step 2. Find the session file
Get-ChildItem "$env:USERPROFILE\.claude\projects" -Recurse -Filter "$sessionId.jsonl"

      ---- OR ----

Remove-Item "$env:USERPROFILE\.claude\projects\E--SuperAdmin\306239f5-df74-4964-8ee8-50340e7fbbf5.jsonl" -Force




How to project from claude 
---------------------------

claude purge "C:\Users\Lenovo\OneDrive\Desktop\loads"











"""