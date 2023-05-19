# Databricks notebook source
#
# COMMAND ----------

diamonds_data = spark.read.format("csv") \
                        .option("inferSchema", "True") \
                        .option("header", "True") \
                        .option("sep", ",") \
                        .load("/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv")

# COMMAND ----------

credit_data = diamonds_data \
           .write.mode('append')\
           .saveAsTable("test_diamonds_data")           
             
