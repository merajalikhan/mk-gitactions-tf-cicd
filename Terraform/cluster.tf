
data "databricks_spark_version" "latest_lts" {
  long_term_support = true
}
resource "databricks_cluster" "shared_autoscaling" {
  cluster_name            = var.cluster_name
  spark_version           = data.databricks_spark_version.latest_lts.id #"12.2 LTS (includes Apache Spark 3.3.2, Scala 2.12)"
  node_type_id            = "Standard_DS3_v2"
  autotermination_minutes = 10   
  num_workers = 1
  
}

resource "databricks_cluster" "shared_autoscaling1" {
  cluster_name            = "KG Cluster"
  spark_version           = data.databricks_spark_version.latest_lts.id #"12.2 LTS (includes Apache Spark 3.3.2, Scala 2.12)"
  node_type_id            = "Standard_DS3_v2"
  autotermination_minutes = 15   
  num_workers = 1
 
  
}


output "cluster_id" {
 value = databricks_cluster.shared_autoscaling.id
}


 