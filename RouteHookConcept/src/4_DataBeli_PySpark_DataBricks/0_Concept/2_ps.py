"""

Spark Deployment Modes
======================


There are three commonly used deployment modes of Spark:

1. Local Mode
2. Client Mode
3. Cluster Mode


Local Mode
----------

If the Driver and Executors run on the same machine,
it is called Local Deployment Mode.

Local Mode is mainly used for:

. Learning
. Development
. Testing
. Debugging


|-------------------------|
|                         |
|       Client            |
|                         |
|       Driver            |
|                         |
|       Executor          |
|                         |
|       Executor          |
|                         |
|-------------------------|


Note:
In Local Mode, Spark runs on a single machine and does not
require a separate cluster of worker nodes.


Client Mode
-----------

If the Client and Driver run on one machine,
while the Executors run on different machines in the cluster,
it is called Client Deployment Mode.


|-------------------------|
|                         |
|       Client            |
|                         |
|       Driver            |
|                         |
|-------------------------|


|-------------------------|
|                         |
|    Cluster Manager      |
|                         |
|    Worker Node          |
|                         |
|    Executor             |
|    Executor             |
|    Executor             |
|                         |
|-------------------------|


In Client Mode:

. Client and Driver are outside the cluster.
. Driver communicates with the Cluster Manager.
. Executors run inside the cluster.
. Driver remains running on the client machine.


Cluster Mode
------------

If the Client runs on one machine,
while the Driver and Executors run inside the cluster,
it is called Cluster Deployment Mode.


|-------------------------|
|                         |
|       Client            |
|                         |
|-------------------------|


|-------------------------|
|                         |
|    Cluster Manager      |
|                         |
|       Driver            |
|                         |
|    Worker Node          |
|                         |
|    Executor             |
|                         |
|    Executor             |
|                         |
|-------------------------|


In Cluster Mode:

. Client is outside the cluster.
. Driver runs inside the cluster.
. Executors run inside the cluster.
. Client submits the application and does not need
  to keep the Driver running locally.


Important Difference
====================

Client Mode:
Client + Driver  -> Outside Cluster
Executors        -> Inside Cluster


Cluster Mode:
Client           -> Outside Cluster
Driver + Executors -> Inside Cluster


Easy Way to Remember:

Client Mode  -> Driver is on Client Machine.

Cluster Mode -> Driver is inside Cluster.


"""