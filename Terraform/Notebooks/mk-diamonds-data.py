# Databricks notebook source
#

# COMMAND ----------

diamonds_data = spark.read.format("csv") \
                        .option("inferSchema", "True") \
                        .option("header", "True") \
                        .option("sep", ",") \
                        .load("/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv")

# COMMAND ----------

diamonds_data = diamonds_data \
           .write.mode('append')\
           .saveAsTable("test_diamonds_data")           
             

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
