"""


Spark APIs
==========


There are mainly two types of APIs in Spark:

1. Low-Level APIs
2. Structured APIs


Low-Level APIs
--------------

RDD (Resilient Distributed Dataset)
Distributed Variables


RDD:
----
RDD is a distributed collection of data that can be processed
in parallel across multiple machines.


Distributed Variables:
----------------------

. Broadcast Variables
. Accumulators


Structured APIs
---------------

DataFrame
Dataset
SQL


DataFrame:
----------
A DataFrame is a distributed collection of data organized
into named columns, similar to a table in a database.


Dataset:
--------
Dataset provides a strongly typed API.

Note:
Dataset API is mainly available in Scala and Java.
Python does not have a Dataset API.


SQL:
----
Spark SQL allows us to use SQL queries to process
structured and semi-structured data.


Spark Libraries
---------------

Structured Streaming
MLlib
GraphX
SparkR


Structured Streaming:
---------------------

Structured Streaming is Spark's scalable and fault-tolerant
stream processing engine built on Spark SQL and DataFrame APIs.


MLlib:
------

MLlib is Spark's machine learning library.

It provides algorithms and tools for:

. Classification
. Regression
. Clustering
. Recommendation
. Feature Engineering


GraphX:
-------

GraphX is Spark's library for graph processing and
graph-parallel computation.


SparkR:
-------

SparkR is an R package that provides an R API for Spark.


Important:
----------

Low-Level APIs:
. RDD
. Distributed Variables


Structured APIs:
. DataFrame
. Dataset
. SQL


Other Spark Libraries:
. Structured Streaming
. MLlib
. GraphX
. SparkR


"""