

# mysql.connector.connect() 
#---------------------------

# There are five attribute in mysql.connector.connect() method

# 1. host : where database server run
# 2. user : username of that machine
# 3. password :
# 4. database : name of database on that server


# mysql.connector.connect(host='localhost', user='root', password='', database='world')


import pandas as pd
from sqlalchemy import create_engine  # <- must import create_engine

# Create SQLAlchemy engine
engine = create_engine("mysql+pymysql://root:@127.0.0.1/world")

# Query
query = "SELECT * FROM city LIMIT 5"

# Load into Pandas DataFrame
df = pd.read_sql(query, engine)

print(df)