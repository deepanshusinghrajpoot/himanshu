'''


# ================================
# Topic: Read JSON & CSV in PySpark
# ================================

# List files in directory
# Role: Show available files in path
dbutils.fs.ls('/Volumes/workspace/landing/data_file/')




# -------------------------------
# Read JSON file
# -------------------------------
df_json = spark.read \
    .format('json') \                # Role: Define file type (JSON)
    .option('inferSchema', True) \   # Role: Auto detect data types
    .option('header', True) \        # Role: First row as column (not used in JSON)
    .option('multiline', False) \    # Role: Read single-line JSON
    .load('/Volumes/workspace/landing/data_file/drivers.json')  # Role: Load data

df_json.display()   # Role: Show DataFrame




# -------------------------------
# Read CSV file
# -------------------------------
df_csv = spark.read \
    .format('csv') \                 # Role: Define file type (CSV)
    .option('inferSchema', True) \   # Role: Auto detect data types
    .option('header', True) \        # Role: First row as column names
    .load('/Volumes/workspace/landing/data_file/BigMart Sales.csv')  # Role: Load data

df_csv.display()   # Role: Show DataFrame






# ================================
# Objective of Methods
# ================================

# spark.read     → Start reading data
# format()       → Specify file type (json, csv, etc.)
# option()       → Set extra settings (schema, header, multiline)
# load()         → Load file into DataFrame
# display()      → Show data (Databricks)
# show()         → Show data (VS Code)





'''