resource "aws_ecs_cluster" "coffee_db_cluster" {
  name = "coffee_db" # Naming the cluster
}

resource "aws_ecs_service" "my_first_service" {
  name            = "coffee-db"                             # Naming our first service
  cluster         = "${aws_ecs_cluster.coffee_db_cluster.id}"             # Referencing our created Cluster
  task_definition = "${aws_ecs_task_definition.coffee_db_task.arn}" # Referencing the task our service will spin up
  launch_type     = "FARGATE"
  desired_count   = 1 # Setting the number of containers we want deployed to 3

  network_configuration {
    subnets          = ["${aws_default_subnet.default_subnet_a.id}"]
    assign_public_ip = true # Providing our containers with public IPs
  }
}