

"""






What is Parquet

Performance Comparison with CSV

Row vs Columnar Format

Parquet Internals

Hands on with Spark



What is Parquet Format
----------------------

Apache Parquet is an open source, column-oriented data file format designed for 
efficient data storage and retrieval.

The Parquet file format was developed in 2013 as a result of a collaboration between
engineers at Twitter and Cloudera.

It was created to provide a more efficient columnar storage solution for 
big data workloads, building upon previous work from Doug Cutting.



Dataset             | Size         | Query Run Time      | Data Scanned           | Cost           |
----------------------------------------------------------------------------------------------------
Data stored as CSV  | 1024 GB      | 236 seconds         | 1177 GB                | $5.75          |
files               |              |                     |                        |                |
Data stored in      | 130 GB       | 6.78 seconds        | 2.51 GB                | $0.01          |
Apache Parquet      |              |                     |                        |                |
Format              |              |                     |                        |                |
Saving              |87% less when | 34x faster          | 99% less data scanned  | 99.7% savings  |
                    |using Parquet |                     |                        |                |




Row format

Columnar format

Row Groups

Internals




Parquet is one of the columnar format whit other some inhancement or feature

we know within parquet the data
it is store as row groups and within row groups data 
store column wise

and apart from storing data columnar format 
within each groups it store a footer witch store meta data about group
like there type, encoding, offset 
along with this footer also contain profiling details
that mean what is minimum value of column, what is maximum value of column
how many null store ther those kind of details also within footor


give example 


"""