# Databricks notebook source
tableName   = "diamonds"
dbName      = "default"
columnName  = "clarity"
columnValue = "VVS2"

import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def tableExists(tableName, dbName):  
  returnValue=  spark.catalog.tableExists(f"{dbName}.{tableName}")
  if returnValue == True:
    print(f"Table '{tableName}' exist in database '{dbName}'.") 
  else:
    print(f"Table '{tableName}' does not exist in database '{dbName}'.")   
  return  returnValue

def columnExists(dataFrame, tableName, columnName):
  if columnName in dataFrame.columns: 
    print(f"Column '{columnName}' exist in table '{tableName}' .") 
    return True
  else:
    print(f"Column '{columnName}' does not exist in table '{tableName}'.")   
    return False

def numRowsInColumnForValue(dataFrame, tableName, columnName, columnValue):
  df = dataFrame.filter(col(columnName) == columnValue)
  numRows = df.count()
  print(f"There are {numRows} rows in '{tableName}' where '{columnName}' equals '{columnValue}'.")
  return numRows

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
        self.assertEqual(numRowsInColumnForValue(df, tableName, columnName, columnValue), 5066)  

r = unittest.main(argv=[''], verbosity=2, exit=False)
assert r.result.wasSuccessful(), 'Test failed; see logs above'
