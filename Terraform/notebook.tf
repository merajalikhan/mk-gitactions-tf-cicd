
## Deply all notebooks from the Notebooks folder
resource "databricks_notebook" "all_notebooks" {
    for_each = fileset("${path.module}/Notebooks", "*") 
    source   = "Notebooks/${each.value}"
    path     = "/${var.all_notebook_folder}/${each.value}"
    language = var.notebook_language  
  }

## Deply all notebooks from the Notebooks/UnitTests folder
resource "databricks_notebook" "test_notebooks" {
    for_each = fileset("${path.module}/Notebooks/UnitTests", "*") 
    source   = "Notebooks/UnitTests/${each.value}"
    path     = "/${var.unit_tests_notebook_folder}/${each.value}"
    language = var.notebook_language  
  }

## Get the notebook data for all  deployed notebooks
data "databricks_notebook" "all_notebooks_data" {
    depends_on = [ databricks_notebook.all_notebooks ]
    for_each = fileset("${path.module}/Notebooks", "*") 
    path="/${var.all_notebook_folder}/${each.value}"
    format = "SOURCE"
  }


  /*
resource "databricks_notebook" "nb1" {
  path     = "${data.databricks_current_user.logged_in_user.home}/${var.notebook_subdirectory}/${var.notebook_filename}"
  language = var.notebook_language
  source   = "./${var.notebooks_folder}/${var.notebook_filename}"
}
*/

/*
resource "databricks_notebook" "nb2" {
  #path     = "${data.databricks_current_user.logged_in_user.home}/${var.notebook_subdirectory}/mk-test-notebook.py"
  path     = "/${var.notebook_subdirectory}/mk-test-notebook.py"
  language = var.notebook_language
  source   = "./${var.notebooks_folder}/mk-test-notebook.py"
}

output "notebook_url" {
 value = databricks_notebook.nb2.url
}

*/
