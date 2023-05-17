# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE DATABASE IF NOT EXISTS CreditDataWarehouse

# COMMAND ----------

dbutils.fs.ls("dbfs:/")

# COMMAND ----------

df1 = spark.read.format("csv").load("dbfs:/FileStore/shared_uploads/credit_train.csv")


# COMMAND ----------

credit_data = spark.read.format("csv") \
                        .option("inferSchema", "True") \
                        .option("header", "True") \
                        .option("sep", ",") \
                        .load("dbfs:/FileStore/shared_uploads/credit_train.csv")

# COMMAND ----------

from pyspark.sql.types import StructField, StructType, StringType,LongType

custom_schema = StructType([
    StructField("CustomerID", StringType(), True),
    StructField("Income", StringType(), True),
    StructField("MonthlyDebtPayment", StringType(), True),
])


# COMMAND ----------

credit_data = spark.read.format("csv") \
                        .schema(custom_schema)\
                        .option("header", "True")\
                        .option("sep", ",") \
                        .load("dbfs:/FileStore/shared_uploads/credit_train.csv")

# COMMAND ----------

credit_data.printSchema()

# COMMAND ----------

credit_data.show(5)

# COMMAND ----------

credit_data = credit_data \
           .write.mode('append')\
           .saveAsTable("creditdatawarehouse.credit_data_monthly_debt")           

# COMMAND ----------

diamonds_data = spark.read.format("csv") \
                        .option("inferSchema", "True") \
                        .option("header", "True") \
                        .option("sep", ",") \
                        .load("/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv")

# COMMAND ----------

diamonds_data.select('carat','cut','color','clarity').filter('cut = "Premium"').show() 

# COMMAND ----------

diamonds_data.select('carat','cut','color','clarity').filter('cut = "Premium"')\
             .write.mode("append")\
             .saveAsTable("creditdatawarehouse.diamonds_data")

# COMMAND ----------

diamonds_data.select('carat','cut','color','clarity').filter('cut = "Premium"')\
             .write.mode("append")\
             .saveAsTable("creditdatawarehouse.diamonds_data_test")
             
