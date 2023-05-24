# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE DATABASE IF NOT EXISTS mktest_db

# COMMAND ----------

diamonds_data = spark.read.format("csv") \
                        .option("inferSchema", "True") \
                        .option("header", "True") \
                        .option("sep", ",") \
                        .load("/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv")

# COMMAND ----------

diamonds_data = diamonds_data \
           .write.mode('append')\
           .saveAsTable("mktest_db.all_diamonds_data")           
             

# COMMAND ----------

diamonds_data.select('carat','cut','color','clarity').filter('cut = "Premium"').show() 

# COMMAND ----------

diamonds_data.select('carat','cut','color','clarity').filter('cut = "Premium"')\
             .write.mode("append")\
             .saveAsTable("mktest_db.selected_col_diamonds_data")

# COMMAND ----------


