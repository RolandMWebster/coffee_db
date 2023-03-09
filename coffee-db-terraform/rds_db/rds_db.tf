resource "aws_db_instance" "coffee_db" {
  allocated_storage      = 5
  db_name                = "coffee_db_rds"
  engine                 = "postgres"
  instance_class         = "db.t3.micro"
  username               = var.rds_username
  password               = var.rds_password
  skip_final_snapshot    = true
  vpc_security_group_ids = ["${aws_security_group.rds_security_group.id}"]
  publicly_accessible    = true
}