"""


Reading CSV Files in PySpark
============================


Reading simple CSV files using spark.read.csv()
and spark.read.format("csv").load()
------------------------------------------------

There are two common ways to read CSV files in PySpark.


First way
.........

df = spark.read.csv(
    "/Volumes/my_files/my_schema/csv_files/my_files/sales.csv"
)

display(df)


Second way
..........

df = spark.read.format("csv").load(
    "/Volumes/my_files/my_schema/csv_files/my_files/sales.csv"
)

display(df)


Note:
By default:

. header = false
. inferSchema = false
. delimiter = ","

Therefore, Spark treats the first row as data and
all columns are initially read as StringType.


Example CSV
-----------

id,customer_name,product,quantity,price
1,John,Laptop,2,50000
2,Rahul,Mouse,3,500
3,Amit,Keyboard,1,1200


Output without header option
----------------------------

+---+-------------+--------+--------+------+
|_c0|_c1          |_c2     |_c3     |_c4   |
+---+-------------+--------+--------+------+
|id |customer_name|product |quantity|price |
|1  |John         |Laptop  |2       |50000 |
|2  |Rahul        |Mouse   |3       |500   |
|3  |Amit         |Keyboard|1       |1200  |
+---+-------------+--------+--------+------+



Handling headers with .option("header", "true")
------------------------------------------------

df = spark.read\
     .option("header", "true")\
     .csv("/Volumes/my_files/my_schema/csv_files/my_files/sales.csv")

display(df)


Output
------

+---+-------------+--------+--------+-----+
|id |customer_name|product |quantity|price|
+---+-------------+--------+--------+-----+
|1  |John         |Laptop  |2       |50000|
|2  |Rahul        |Mouse   |3       |500  |
|3  |Amit         |Keyboard|1       |1200 |
+---+-------------+--------+--------+-----+


Note:
header = true tells Spark that the first row contains
column names and should not be treated as data.



Inferring schema automatically with .option("inferSchema", "true")
-------------------------------------------------------------------

df = spark.read\
    .option("header", "true")\
    .option("inferSchema", "true")\
    .csv("/Volumes/my_files/my_schema/csv_files/my_files/sales.csv")

display(df)


Output Schema
-------------

root
 |-- id: integer
 |-- customer_name: string
 |-- product: string
 |-- quantity: integer
 |-- price: integer


Output
------

+---+-------------+--------+--------+-----+
|id |customer_name|product |quantity|price|
+---+-------------+--------+--------+-----+
|1  |John         |Laptop  |2       |50000|
|2  |Rahul        |Mouse   |3       |500  |
|3  |Amit         |Keyboard|1       |1200 |
+---+-------------+--------+--------+-----+


Note:
inferSchema = true tells Spark to automatically determine
the data type of each column by examining the data.


Important:
inferSchema can be convenient for exploration, but in
production pipelines it is generally better to define
the schema explicitly.



Providing your own schema manually
(String and StructType methods)
---------------------------------

There are two common ways to provide a schema manually.


First way: Using String Schema
................................

schema_str = "
     id INT,
     customer_name STRING,
     product STRING,
     quantity INT,
     price DOUBLE,
     remarks STRING
"

df = spark.read\
    .option("header", "true")\
    .schema(schema_str)\
    .csv("/Volumes/my_files/my_schema/csv_files/my_files/sales.csv")

display(df)



Second way: Using StructType
.............................

from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType,
    DoubleType
)


schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("customer_name", StringType(), True),
    StructField("product", StringType(), True),
    StructField("quantity", IntegerType(), True),
    StructField("price", DoubleType(), True),
    StructField("remarks", StringType(), True)
])


df = spark.read\
    .option("header", "true")\
    .schema(schema)\
    .csv("/Volumes/my_files/my_schema/csv_files/my_files/sales.csv")

display(df)


Output Schema
-------------

root
 |-- id: integer
 |-- customer_name: string
 |-- product: string
 |-- quantity: integer
 |-- price: double
 |-- remarks: string


Important:
The third argument of StructField is nullable.

True  -> Column can contain NULL values.
False -> Column should not contain NULL values.


Example:

StructField("id", IntegerType(), True)

. id          -> Column name
. IntegerType -> Data type
. True        -> Nullable



Handling pipe (|) delimited files
using .option("delimiter", "|")
--------------------------------

df = spark.read\
    .option("header", "true")\
    .option("inferSchema", "true")\
    .option("delimiter", "|")\
    .csv("/Volumes/my_files/my_schema/csv_files/my_files/sales_pipe.csv")

display(df)


Example Input
-------------

id|customer_name|product|quantity|price
1|John|Laptop|2|50000
2|Rahul|Mouse|3|500


Output
------

+---+-------------+-------+--------+-----+
|id |customer_name|product|quantity|price|
+---+-------------+-------+--------+-----+
|1  |John         |Laptop |2       |50000|
|2  |Rahul        |Mouse  |3       |500  |
+---+-------------+-------+--------+-----+


Note:
delimiter = "|" tells Spark that the pipe character
is used to separate columns.



Managing single-quote data using .option("quote", "'")
-------------------------------------------------------

df = spark.read\
    .option("header", "true")\
    .option("inferSchema", "true")\
    .option("delimiter", "|")\
    .option("quote", "'")\
    .csv("/Volumes/my_files/my_schema/csv_files/my_files/sales_pipe_single_quote.csv")

display(df)


Example Input
-------------

id|customer_name|product|remarks
1|'John'|'Laptop'|'Good product'
2|'Rahul'|'Mouse'|'Good quality'


Output
------

+---+-------------+-------+------------+
|id |customer_name|product|remarks     |
+---+-------------+-------+------------+
|1  |John         |Laptop |Good product|
|2  |Rahul        |Mouse  |Good quality|
+---+-------------+-------+------------+


Note:
quote defines the character used to quote fields.



Dealing with escape characters
using .option("escape", "#")
--------------------------------

df = spark.read\
    .option("header", "true")\
    .option("inferSchema", "true")\
    .option("delimiter", "|")\
    .option("quote", "'")\
    .option("escape", "#")\
    .csv("/Volumes/my_files/my_schema/csv_files/my_files/sales_pipe_single_quote_escape.csv")

display(df)


Example Input
-------------

id|customer_name|product|remarks
1|'John'|'Laptop'|'Good #\'product#\''
2|'Rahul'|'Mouse'|'Good quality'


Note:
escape specifies the character used to escape the quote
character inside a quoted field.



Reading multi-line records using .option("multiLine", "true")
--------------------------------------------------------------

df = spark.read\
    .option("header", "true")\
    .option("inferSchema", "true")\
    .option("delimiter", "|")\
    .option("quote", "'")\
    .option("escape", "#")\
    .option("multiLine", "true")\
    .csv("/Volumes/my_files/my_schema/csv_files/my_files/sales_pipe_single_quote_escape_multiline.csv")

display(df)


Example Input
-------------

id|customer_name|product|remarks
1|John|Laptop|'Good product
with multiple lines'
2|Rahul|Mouse|'Good quality'


Output
------

+---+-------------+-------+-------------------------+
|id |customer_name|product|remarks                  |
+---+-------------+-------+-------------------------+
|1  |John         |Laptop |Good product             |
|   |             |       |with multiple lines      |
|2  |Rahul        |Mouse  |Good quality             |
+---+-------------+-------+-------------------------+


Note:
multiLine = true allows a quoted field to contain
line breaks.



Important CSV Read Options
==========================

+----------------+----------------------------------------------+
| Option         | Purpose                                      |
+----------------+----------------------------------------------+
| header         | Uses first row as column names              |
| inferSchema    | Automatically detects column data types     |
| delimiter      | Defines the column separator                 |
| quote          | Defines the quote character                 |
| escape         | Defines the escape character                |
| multiLine      | Allows records to span multiple lines       |
| nullValue      | Defines the string that represents NULL      |
| mode            | Defines how malformed records are handled   |
+----------------+----------------------------------------------+



Common mode options
-------------------

mode = "PERMISSIVE"
. Keeps malformed records and tries to parse them.

mode = "DROPMALFORMED"
. Drops malformed records.

mode = "FAILFAST"
. Stops reading when a malformed record is found.



Original CSV Input
==================

id,customer_name,product,quantity,price
1,John,Laptop,2,50000
2,Rahul,Mouse,3,500
3,Amit,Keyboard,1,1200


Spark Code
==========

df = spark.read\
    .option("header", "true")\
    .option("inferSchema", "true")\
    .csv("sales.csv")


Output Table
============

+---+-------------+--------+--------+-----+
|id |customer_name|product |quantity|price|
+---+-------------+--------+--------+-----+
|1  |John         |Laptop  |2       |50000|
|2  |Rahul        |Mouse   |3       |500  |
|3  |Amit         |Keyboard|1       |1200 |
+---+-------------+--------+--------+-----+


Output Schema
=============

root
 |-- id: integer
 |-- customer_name: string
 |-- product: string
 |-- quantity: integer
 |-- price: integer


Important Best Practices
========================

1. Use header = true when the CSV contains a header.

2. Prefer an explicit schema for production pipelines.

3. Use inferSchema = true mainly when exploring data
   or when the schema is not known.

4. Specify delimiter when the file is not comma-separated.

5. Use quote and escape when CSV fields contain
   special characters.

6. Use multiLine = true when a quoted field can contain
   line breaks.

7. Use the correct mode to handle malformed records.





| Option        | Meaning                              | Example                                   |
|---------------|--------------------------------------|-------------------------------------------|
| `header`      | First row contains column names      | `.option("header", "true")`               |
| `inferSchema` | Automatically detects data types     | `.option("inferSchema", "true")`          |
| `schema`      | Provides your own schema             | `.schema(schema)`                         |
| `delimiter`   | Column separator                     | `.option("delimiter", "|")`               |
| `quote`       | Quote character                      | `.option("quote", "'")`                   |
| `escape`      | Escape character                     | `.option("escape", "#")`                  |
| `multiLine`   | Allows records across multiple lines | `.option("multiLine", "true")`            |
| `nullValue`   | String treated as NULL               | `.option("nullValue", "NA")`              |
| `mode`        | Handles malformed records            | `PERMISSIVE`, `DROPMALFORMED`, `FAILFAST` |




🔥 Most important for interview
--------------------------------

Remember this pattern:

df = spark.read\    
     .option("header", "true")\    
     .option("inferSchema", "true")\    
     .option("delimiter", ",")\    
     .csv("sales.csv")


And for production, remember:

CSV
 ↓
Explicit Schema
 ↓
DataFrame
 ↓
Validation / Cleaning
 ↓
Transformation

One small point: display(df) is commonly available in Databricks notebooks. 
In standard PySpark environments, use df.show() instead.



"""