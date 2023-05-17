terraform {
  required_providers {    
    databricks = {
      source = "databricks/databricks"
    }
  }

  #specifies which Terraform Cloud workspaces to use for  accessing shared state and any environment variables.
 
#  cloud {
#    organization = "mk-test-organisation"
#    workspaces {
#      name = "mk-gitactions-tf-cicd"
#    }    
  #}
  
  backend "remote" {
    hostname     = "app.terraform.io"
    organization = "mk-test-organisation"
    workspaces { prefix = "mk-git-actions-tf-api-" }
  }
}

provider "databricks" {
  #host =   var.databricks_host
  #token =  var.databricks_token
}



//data "databricks_current_user" "logged_in_user" {}

data "databricks_cluster" "my_cluster" {
  cluster_name = databricks_cluster.shared_autoscaling.cluster_name #var.cluster_name
  } 
