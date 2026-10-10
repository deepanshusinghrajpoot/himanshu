"""

Spark Architecture
===================


                            |--------------------------------------------|
                            |                                            |
                            |              Worker Node                   |
                            |              (Executor 1)                  |
                            |                                            |
                            |--------------------------------------------|
                                         ^
                                         |
                                         |
Client ----------------> Driver <------> Cluster Manager
                         (Driver Node)       |
                              |               |
                              |               |
                              |               v
                              |--------------------------------------------|
                              |                                            |
                              |              Worker Node                   |
                              |              (Executor 2)                  |
                              |                                            |
                              |--------------------------------------------|



Client:
-------

In the client, we write our Spark code and submit the application.

Code can be written using different languages such as:

. Python
. Scala
. Java
. SQL
. R


Driver:
-------

After submitting the application, the Spark application starts
with a Driver.

The Driver is responsible for:

. Understanding the application code
. Creating the execution plan
. Dividing the application into jobs, stages, and tasks
. Requesting resources from the Cluster Manager
. Scheduling tasks on Executors
. Tracking the execution of the application
. Collecting the final results


Cluster Manager:
----------------

The Driver requests resources from the Cluster Manager.

The Cluster Manager manages the resources of the cluster
and provides resources to run Executors on Worker Nodes.

Examples of Cluster Managers:

. Standalone
. YARN
. Kubernetes
. Mesos


Worker Node:
------------

A Worker Node is a machine in the cluster where Spark Executors
run.

One Worker Node can have one or more Executors.


Executor:
---------

An Executor is a process that runs on a Worker Node.

The Executor is responsible for:

. Executing tasks assigned by the Driver
. Processing data
. Storing intermediate data in memory or disk
. Sending results/status back to the Driver


Execution Flow:
---------------

1. Client submits the Spark application.

2. Driver starts and understands the application code.

3. Driver creates the execution plan.

4. Driver requests resources from the Cluster Manager.

5. Cluster Manager allocates resources and starts Executors
   on Worker Nodes.

6. Driver sends tasks to the Executors.

7. Executors process the data in parallel.

8. Executors send results/status information back to the Driver.

9. Driver coordinates and manages the complete application.


Spark Context:
--------------

SparkContext is an object created in the Driver.

It acts as an entry point for Spark's core functionality
and allows the Driver to communicate with the Spark cluster.

Note:
In modern Spark applications, SparkSession is commonly used
as the main entry point instead of directly using SparkContext.


Important:
----------

. Driver -> Controls and coordinates the Spark application.

. Cluster Manager -> Allocates cluster resources.

. Worker Node -> Machine where Executors run.

. Executor -> Process that executes tasks.

. One Worker Node can have multiple Executors.

. One Spark application has one Driver and can have multiple Executors.

. Driver and Executors together form a Spark application.

"""