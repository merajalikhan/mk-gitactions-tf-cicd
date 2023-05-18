# Databricks notebook source
print ('mk test notebook!!')

# COMMAND ----------

credit_data = spark.read.format("csv") \
                        .schema(custom_schema)\
                        .option("header", "True")\
                        .option("sep", ",") \
                        .load("dbfs:/FileStore/shared_uploads/credit_train.csv")

# COMMAND ----------

credit_data = credit_data \
           .write.mode('append')\
           .saveAsTable("creditdatawarehouse.credit_data_monthly_debt")
