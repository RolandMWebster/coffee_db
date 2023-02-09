resource "aws_ecr_repository" "coffee_db" {
  name                 = "coffee_db"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}