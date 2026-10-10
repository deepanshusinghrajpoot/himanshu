"""
What is Spark
=============

Spark is a unified and open-source compute engine for parallel
data processing with multiple language libraries.


Unified means it can perform different types of data processing

. Batch Processing
. Stream Processing
. Machine Learning
. Graph Processing


Why Spark is popular
====================

1. Unified
2. Speed
3. Multi-language support


Speed:
-------
Spark can be much faster than traditional Hadoop MapReduce
for many workloads because Spark can keep intermediate data
in memory instead of repeatedly writing it to disk.

Note:
Spark is not always 100 times faster. The actual performance
depends on the workload, data size, cluster configuration,
and processing method.


Multi-language support:
-----------------------

Spark itself is mainly written in Scala.

Spark provides APIs for multiple languages such as:

. Python       -> PySpark
. Scala
. Java
. R


Important:
Spark is mainly used for large-scale distributed data processing.
It divides the data and processing work across multiple machines
in a cluster, which allows parallel processing.


"""