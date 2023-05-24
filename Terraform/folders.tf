resource "databricks_directory" "unit_test_directory" {
  path = "Shared/GitHubActionsTFTests/UnitTestNotebooks"
}
resource "databricks_directory" "notebooks_directory" {
  path = "Shared/GitHubActionsTFTests/Notebooks"
}