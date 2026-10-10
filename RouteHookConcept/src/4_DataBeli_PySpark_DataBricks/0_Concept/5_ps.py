"""


Read JSON Data
==============

Spark can read JSON data using spark.read.json().

There are two common ways to read JSON data:

1. Single-line JSON
2. Multi-line JSON


Read single-line JSON file
--------------------------

df = spark.read.json(
    "/Volumes/my_files/my_schema/csv_files/my_files/sales_single_line.json"
)

display(df)


Example JSON
------------

{"id":1,"customer_name":"John","product":"Laptop","price":50000}
{"id":2,"customer_name":"Rahul","product":"Mouse","price":500}
{"id":3,"customer_name":"Amit","product":"Keyboard","price":1200}


Note:
By default, Spark expects each JSON record to be on a
separate line.

This is also called JSON Lines / NDJSON format.



Read multi-line JSON file
-------------------------

df = spark.read\
    .option("multiLine", "true")\
    .json("/Volumes/my_files/my_schema/csv_files/my_files/sales_multi_line.json")

display(df)


Example JSON
------------

[
    {
        "id": 1,
        "customer_name": "John",
        "product": "Laptop",
        "price": 50000
    },
    {
        "id": 2,
        "customer_name": "Rahul",
        "product": "Mouse",
        "price": 500
    }
]


Note:
multiLine = true allows Spark to read a JSON record
that spans multiple lines.

It is commonly used when the JSON data is formatted
as a multi-line JSON object or array.



Write JSON data at a specific location
--------------------------------------

df.write.format("json")\
    .save("/Volumes/my_files/my_schema/csv_files/my_files/sales_json")


The above code writes the DataFrame in JSON format.


Output Location
---------------

sales_json/
    part-00000-................json
    part-00001-................json
    _SUCCESS


Important:
Spark writes the output as a directory containing
one or more part files.

The number of part files depends on the number of
output partitions.



Write JSON using .json()
------------------------

We can also use the shorter syntax:

df.write\
    .json("/Volumes/my_files/my_schema/csv_files/my_files/sales_json")


Both are equivalent:

df.write.format("json").save("path")

df.write.json("path")



Write JSON with overwrite mode
------------------------------

df.write\
    .mode("overwrite")\
    .json("/Volumes/my_files/my_schema/csv_files/my_files/sales_json")


Common write modes:

. append
. overwrite
. ignore
. error / errorifexists


Note:
The default mode is "errorifexists".



Write data in the form of CSV
-----------------------------

df.write.format("csv")\
    .save("/Volumes/my_files/my_schema/csv_files/my_files/sales_csv")


We can also use the shorter syntax:

df.write\
    .csv("/Volumes/my_files/my_schema/csv_files/my_files/sales_csv")


Output Location
---------------

sales_csv/
    part-00000-................csv
    part-00001-................csv
    _SUCCESS



Writing CSV with header
-----------------------

df.write\
    .option("header", "true")\
    .csv("/Volumes/my_files/my_schema/csv_files/my_files/sales_csv")


Output CSV
----------

id,customer_name,product,price
1,John,Laptop,50000
2,Rahul,Mouse,500
3,Amit,Keyboard,1200



Writing CSV with overwrite mode
--------------------------------

df.write\
    .mode("overwrite")\
    .option("header", "true")\
    .csv("/Volumes/my_files/my_schema/csv_files/my_files/sales_csv")



Important Difference
====================

Reading JSON:

spark.read.json("path")


Reading JSON with options:

spark.read\
    .option("multiLine", "true")\
    .json("path")


Writing JSON:

df.write.json("path")


Writing CSV:

df.write.csv("path")


Writing using format():

df.write.format("json").save("path")

df.write.format("csv").save("path")



Important:
==========

Spark DataFrame writes are distributed.

Therefore, when we write data:

df.write.json("path")

Spark usually creates a directory containing
multiple part files instead of creating a single file.


If we specifically need a single output file,
we can reduce the number of partitions:

df.coalesce(1)\
    .write\
    .mode("overwrite")\
    .option("header", "true")\
    .csv("output_path")


Note:
coalesce(1) should be used carefully for large datasets
because it moves the output through a single partition
and can become a performance bottleneck.


"""