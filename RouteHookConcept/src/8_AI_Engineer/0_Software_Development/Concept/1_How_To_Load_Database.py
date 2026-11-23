"""



"D:\xampp\mysql\bin\mysql.exe" -u truckmitr -p truckmitr <"D:\FOR_TRUCKMITR\truckmitr_sql_file\truckmitr.sql"


"D:\xampp\mysql\bin\mysql.exe" -u truckmitr -p"" -P 3307 truckmitr < "D:\FOR_TRUCKMITR\truckmitr_sql_file\truckmitr.sql"




1. Mac equivalent command

Your XAMPP MySQL client is generally located here:
/Applications/XAMPP/xamppfiles/bin/mysql


If your SQL file is in Downloads, use:
/Applications/XAMPP/xamppfiles/bin/mysql -u truckmitr -p -P 3306 truckmitr < ~/Downloads/truckmitr.sql






Next step: confirm the server version

In phpMyAdmin:
1. Click SQL.
2. Execute this read-only query:

SELECT VERSION() AS server_version, @@port AS server_port;
    
   | server_version  | server_port |
eg | 10.4.32-MariaDB | 3307        |
   | --------------- | ----------- |




   










"""