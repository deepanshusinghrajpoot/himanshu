"""


What is MCP
===========

MCP(Model Context Protocol) is an open standard created by Antropic that acts
as a universal connector between claude code and external tools, services, and
data sources.

The key idea to provide claude code with more tools




Plan of Action
==============

Integrate 3 MCP servers to our current project:

DBHub
Figma
Github

Discuss about 7 more MCP servers



MCP Server For Database 
-----------------------

Integration
...........

claude mcp add --transport stdio mysql-db -- npx -y @executeautomation/database-server --mysql --host 127.0.0.1 --database <DB_Name> --port <Port> --user <User_Name> --password "<Password>"

eg:

claude mcp add --transport stdio mysql-db -- npx -y @executeautomation/database-server --mysql --host 127.0.0.1 --database truckmitr --port 3307 --user truckmitr --password "YOUR_ACTUAL_PASSWORD"

Remove 
......

claude mcp remove mysql-db






MCP Server For Figma Design
---------------------------


Integration
...........

claude plugin install figma@claude-plugins-official

After start Claude go int to /plugins
Then Installed


Remove 
......

claude mcp remove mysql-db













"""