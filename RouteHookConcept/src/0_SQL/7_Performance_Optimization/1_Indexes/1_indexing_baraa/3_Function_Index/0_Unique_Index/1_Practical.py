'''




 
 
                                                  Index Syntax
                                        ==============================

In SQL Server
-------------
            
CREATE [UNIQUE] [CLUSTERED | NONCLUSTERED] [COLUMNSTORE] INDEX index_name
ON table_name (column1, column2, ....)



                          |
Index Allows ------------>| CREATE INDEX idx_tableName_columnName 
Duplicate                 | ON tableName (columnName) 

                          |
Duplicates   ------------>| CREATE UNIQUE INDEX idx_tableName_columnName 
are not allowed           | ON tableName (columnName) 




In MySQL Workbench
------------------

CREATE [UNIQUE] INDEX index_name
ON table_name (column1, column2, ....)



                          |
Index Allows ------------>| CREATE INDEX idx_tableName_columnName 
Duplicate                 | ON tableName (columnName)

                          |
Duplicates   ------------>| CREATE UNIQUE INDEX idx_tableName_columnName 
are not allowed           | ON tableName (columnName)



Additional Points
-----------------

➤ ❌ No CLUSTERED INDEX keyword (InnoDB handles clustering internally via Primary Key)  
➤ ❌ No COLUMNSTORE INDEX support  
➤ ✔ Default index type → B-Tree (Rowstore)  
➤ ✔ PRIMARY KEY automatically creates clustered storage  






eg:

CREATE UNIQUE INDEX idx_empluyees_emp_id 
ON top_50_sql_faang_practice.employees (emp_id);



'''