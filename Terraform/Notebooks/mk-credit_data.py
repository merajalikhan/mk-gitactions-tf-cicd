# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE DATABASE IF NOT EXISTS mktest_db

# COMMAND ----------

dbutils.fs.ls("dbfs:/")

# COMMAND ----------

df1 = spark.read.format("csv").load("dbfs:/FileStore/shared-uploads/credit_train.csv")


# COMMAND ----------

credit_data = spark.read.format("csv") \
                        .option("inferSchema", "True") \
                        .option("header", "True") \
                        .option("sep", ",") \
                        .load("dbfs:/FileStore/shared-uploads/credit_train.csv")

# COMMAND ----------

credit_data.show(5)

# COMMAND ----------

#from pyspark.sql.types import StructField, StructType, StringType,LongType

#custom_schema = StructType([
#    StructField("CustomerID", StringType(), True),
#    StructField("Income", StringType(), True),
#    StructField("MonthlyDebtPayment", StringType(), True),
#])


# COMMAND ----------

#credit_data = spark.read.format("csv") \
#                        .schema(custom_schema)\
#                        .option("header", "True")\
#                        .option("sep", ",") \
#                        .load("dbfs:/FileStore/shared-uploads/credit_train.csv")

# COMMAND ----------

credit_data.printSchema()

# COMMAND ----------

credit_data.show(5)

# COMMAND ----------

     credit_data = credit_data \
           .select('Customer ID', 'Annual Income', 'Monthly Debt')\
           .withColumnRenamed('Customer ID', 'Customer_ID')\
           .withColumnRenamed('Annual Income', 'Income')\
           .withColumnRenamed('Monthly Debt', 'Monthly_Debt_Payment')\
           .write.mode('append')\
           .saveAsTable("mktest_db.credit_data_monthly_debt")           
