
data "databricks_spark_version" "latest_lts" {
  long_term_support = true
}

resource "databricks_cluster" "mk-all-purpose" {
  cluster_name            = var.cluster_name
  spark_version           = data.databricks_spark_version.latest_lts.id #"12.2 LTS (includes Apache Spark 3.3.2, Scala 2.12)"
  node_type_id            = "Standard_DS3_v2"
  autotermination_minutes = 10   
  num_workers = 1  
}

data "databricks_cluster" "my_cluster" {
  cluster_name = databricks_cluster.mk-all-purpose.cluster_name #var.cluster_name
  } 

output "cluster_id" {
 value = databricks_cluster.mk-all-purpose.id
}


resource "databricks_cluster" "mk-all-purpose1" {
  cluster_name            = "test cluster"
  spark_version           = data.databricks_spark_version.latest_lts.id #"12.2 LTS (includes Apache Spark 3.3.2, Scala 2.12)"
  node_type_id            = "Standard_DS3_v2"
  autotermination_minutes = 20   
  num_workers = 1  
}
 