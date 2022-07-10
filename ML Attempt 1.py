# project working on machine learning.
# need access to a large data set. 

import pyodbc
import numpy

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=server_name;'
                      'Database=database_name;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT TOP 1000 * FROM schema.table_name')

for i in cursor:
    print(i)
    
# https://www.w3schools.com/python/python_ml_data_distribution.asp
