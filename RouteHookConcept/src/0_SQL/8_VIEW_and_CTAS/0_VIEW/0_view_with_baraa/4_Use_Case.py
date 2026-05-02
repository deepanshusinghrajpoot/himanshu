'''


  Use Case
  ========

  
  First use case
  ---------------

  Store central, complex query logic in the database

  for access by multiple queries, reducing project complexity.
  


  Orders Table        | Query join ORDER and CUSTOMERS table  -----------> Query Rank          |  Financial analyst was doing this type analysis
                      |                                                                        |
                      | Query join ORDER and CUSTOMERS table  -----------> Query Max Min       |  Budget analyst was doing same type analysis
  Customers Table     |                                                                        |  
                      | Query join ORDER and CUSTOMERS table  -----------> Query Mean          |  Risk analyst was doing same type analysis

  
                      
                                     View

  Orders Table        |                                               |   Query Rank             |  Financial analyst was doing this type analysis
                      |                                               |                          |
                      | Query join ORDER and CUSTOMERS table          |   Query Max Min          |  Budget analyst was doing same type analysis
  Customers Table     |                                               |                          |  
                      |                                               |   Query Mean             |  Risk analyst was doing same type analysis

  
           
  gpt make sort tell ans which we tell directly to interviewer




  
  Second Use case Security
  ------------------------


  We can provide column level security by filter column.
  We can also provide column and row level security by filter row and column.


  
  Third Use Case
  ---------------

  Views can be used as Data Marts in Data Warehouse System because they provide a flexible and efficient
  way to present data.

  
'''