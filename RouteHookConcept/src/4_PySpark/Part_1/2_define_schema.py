"""






# ============================================
# Topic: Define Schema Manually in PySpark
# ============================================

# -------------------------------
# 1. Automatic Schema (inferSchema)
# -------------------------------
df = spark.read.format('csv') \
    .option('inferSchema', True) \   # Role: Auto detect data types
    .option('header', True) \        # Role: First row as column names
    .load('/Volumes/workspace/landing/data_file/BigMart Sales.csv')  # Role: Load data

df.printSchema()   # Role: Show structure of DataFrame


# -------------------------------
# 2. Using DDL Schema (String Format)
# -------------------------------
my_ddl_schema = '''
    Item_Identifier STRING,
    Item_Weight STRING,
    Item_Fat_Content STRING,
    Item_Visibility DOUBLE,
    Item_Type STRING,
    Item_MRP DOUBLE,
    Outlet_Identifier STRING,
    Outlet_Establishment_Year INTEGER,
    Outlet_Size STRING,
    Outlet_Location_Type STRING,
    Outlet_Type STRING,
    Item_Outlet_Sales DOUBLE
'''

df = spark.read.format('csv') \
    .schema(my_ddl_schema) \         # Role: Apply custom schema (DDL format)
    .option('header', True) \        # Role: First row as column names
    .load('/Volumes/workspace/landing/data_file/BigMart Sales.csv')

df.printSchema()   # Role: Verify schema


# -------------------------------
# 3. Using StructType Schema
# -------------------------------
from pyspark.sql.types import *

my_struct_schema = StructType([

    StructField('Item_Identifier', StringType(), True),   # Role: Define column + type + nullable
    StructField('Item_Weight', StringType(), True),
    StructField('Item_Fat_Content', StringType(), True),
    StructField('Item_Visibility', StringType(), True),
    StructField('Item_Type', StringType(), True),
    StructField('Item_MRP', StringType(), True),
    StructField('Outlet_Identifier', StringType(), True),
    StructField('Outlet_Establishment_Year', StringType(), True),
    StructField('Outlet_Size', StringType(), True),
    StructField('Outlet_Location_Type', StringType(), True),
    StructField('Outlet_Type', StringType(), True),
    StructField('Item_Outlet_Sales', StringType(), True)

])

df = spark.read.format('csv') \
    .schema(my_struct_schema) \      # Role: Apply structured schema
    .option('header', True) \        # Role: First row as column names
    .load('/Volumes/workspace/landing/data_file/BigMart Sales.csv')

df.printSchema()   # Role: Verify schema


# ============================================
# Objective of Methods
# ============================================

# inferSchema()  → Automatically detect column data types
# printSchema()  → Display DataFrame structure
# schema()       → Apply custom schema
# StructType()   → Define full schema structure
# StructField()  → Define column name, type, and nullability
# StringType()   → Define data type (string)
# DoubleType()   → Define data type (decimal number)
# IntegerType()  → Define data type (integer)










"""