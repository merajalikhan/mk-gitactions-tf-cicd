# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE DATABASE IF NOT EXISTS mktest_db

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE mktest_db.diamonds_test USING CSV LOCATION '/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv' options (header = true, inferSchema = true)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from diamonds_test where carat=0.22
