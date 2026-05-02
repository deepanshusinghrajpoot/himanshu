'''


----------------------------------------------------------------
                             AGENDA
----------------------------------------------------------------

- What is Spark
- Spark Architecture (Most Important For Interviews)
- Spark Benefits
- Lazy Evaluation
- Jobs, Stages, and Account
- Spark Languages Options
- PySpark Coding - The Real OG





---------------
What is Spark?
---------------

Spark distribute data among the machine.






--------------------
Spark Architecture
--------------------

                                        |-----------------------------> Worker Node
                                        |
Driver program  ----------------> Cluster Manager 
                                        |
                                        |-----------------------------> Worker Node




When we submitted our code it will go to driver node.
It will assesst that code it will break that code in form of transformation, stages, job, task.
then it will hand over all the information to cluster manager.
Suppose hypothetical situation our driver node request to cluster manager to create two worker node.
And all information provided driver program go to cluster manager then go to worker nodes.
These two worker will actually execute those transformation.







------------------------------------------------------
Why do we use spark because we have already hadoope
------------------------------------------------------


Spark
-----

1.  In-Memory Computation
2.  Lazy Evaluation
3.  Fault Tolerant
4.  Partitioning



1.  In-Memory Computation
--------------------------

Hadoop use disk memory so it take lot of time.
But Spark use In-Memory Computation so it is faster.





2.  Lazy Evaluation
--------------------

When we perform transformation it will not imediate execute those transformation.
It will lazy evaluate all those transformation then it will execute all those transformation 
when we hit any action.








3.  Fault Tolerant
-------------------

gpt give perfect definition







4.  Partitioning
-----------------

gpt give perfect definition







'''