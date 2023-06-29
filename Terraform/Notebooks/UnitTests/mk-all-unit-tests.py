# Databricks notebook source
tableName   = "all_diamonds_data"
dbName      = "mktest_db"
columnName  = "clarity"
columnValue = "VVS2"

import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def tableExists(tableName, dbName):  
  try:
    returnValue=  spark.catalog.tableExists(f"{dbName}.{tableName}")
    if returnValue == True:
      print(f"Table '{tableName}' exist in database '{dbName}'.") 
    else:
      print(f"Table '{tableName}' does not exist in database '{dbName}'.")   
    return  returnValue
  except Exception e:
    exit('ERROR: Failed with error  :  {} '.format(e))


def columnExists(dataFrame, tableName, columnName):
  returnValue = False
  try:
    if columnName in dataFrame.columns: 
      print(f"Column '{columnName}' exist in table '{tableName}' .") 
      return True
    else:
      print(f"Column '{columnName}' does not exist in table '{tableName}'.")   
      return False
  except Exception e:
    exit('ERROR: Failed with error  :  {} '.format(e))

def numRowsInColumnForValue(dataFrame, tableName, columnName, columnValue):
  try:
    df = dataFrame.filter(col(columnName) == columnValue)
    numRows = df.count()
    print(f"There are {numRows} rows in '{tableName}' where '{columnName}' equals '{columnValue}'.")
    return numRows
  except Exception e:
    exit('ERROR: Failed with error  :  {} '.format(e))


# COMMAND ----------

import unittest
class TestHelpers(unittest.TestCase):
   
    
    def test_tableExists(self):        
        self.assertEqual(tableExists(tableName, dbName), True)
    
    def test_columnExists(self):
        df = spark.sql(f"SELECT * FROM {dbName}.{tableName}")        
        self.assertEqual(columnExists(df, tableName, columnName), True)

    def test_numRowsInColumnForValue(self):
        df = spark.sql(f"SELECT * FROM {dbName}.{tableName}")        
        self.assertEqual(numRowsInColumnForValue(df, tableName, columnName, columnValue), 50660)  

r = unittest.main(argv=[''], verbosity=2, exit=False)
assert r.result.wasSuccessful(), 'Test failed; see logs above'
