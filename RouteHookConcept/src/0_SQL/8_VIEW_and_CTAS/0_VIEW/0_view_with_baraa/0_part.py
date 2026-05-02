'''





Structure and Hierarchy of Database (DBMS Concept)
=================================================

                        Database System
                           |
                One System → Multiple Databases
                           |
                One Database → Multiple Schemas
                           |
                One Schema → Multiple Objects
                           |
          ----------------------------------------
          |                                      |
       Table Object                          View Object


🎤 Spoken
-----------

lll “In a database system, we can have multiple databases. Each database contains schemas, 
     and each schema contains objects like tables, views, indexes, stored procedures, 
     functions, triggers, and sequences.”



Three-Level Architecture (Database Abstraction)
==============================================

lll The database is divided into three levels to reduce complexity:

                             
                    Physical Level (Internal Level) handled by DBA
                             |
Logical Level (Conceptual Level) handled by Data Engineers like objects (tables, views, indexes, stored procedures, functions, triggers, sequences)
                             |
                    View Level (External Level) handled by Data Analyst, Business Analyst
                             

b

                    







                    
(Internal Layer)
Physical Level :-
- This is the lowest level of the database
- It stores the actual data in physical storage

Accessed By:
- Database Administrator (DBA)

Contains:
- Data Files
- Index Files
- Logs
- Pages / Blocks

Spoken:
"The physical level is where the actual data is stored.
It deals with storage details like files and how data is saved on disk.
This level is mainly managed by the DBA."


(Logical Layer)
Logical Level :-
- This level defines how data is structured
- It is easier to understand than the physical level

Accessed By:
- Developers and Data Engineers

Contains:
- Tables
- Relationships
- Views
- Indexes
- Procedures
- Functions

Spoken:
"The logical level defines how data is organized in the database.
It includes tables, relationships, and indexes that developers work with."



(External Layer)
View Level :-
- This is the highest level of abstraction
- It shows only required data to users

Used By:
- End Users
- Applications
- Business Analysts
- Reporting Tools

            Logical Level
                 |
      --------------------------
      |           |            |
    View1       View2       ViewN
   (User)     (Reports)     (Apps)

Spoken:
"The view level is what users interact with.
It shows only the required data instead of the full database."


Abstraction Concept
==================

Physical Level  →  Logical Level  →  View Level

Key Points:
- Physical Level → High Complexity, Low Abstraction
- Logical Level  → Medium Level
- View Level     → High Abstraction

Spoken:
"Abstraction means hiding internal complexity
and showing only the necessary information to the user."


Final Hierarchy
===============

                    Database
                       |
                 Physical Level
                       |
                 Logical Level
                       |
                 View Level
          ----------------------------
          |            |             |
        View1        View2        ViewN


Final Takeaway (Interview Line)
==============================

"A database system is divided into three levels:
physical, logical, and view level.
The physical level handles storage,
the logical level defines structure,
and the view level presents data to users."








'''