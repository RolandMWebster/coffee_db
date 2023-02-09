data "aws_ami" "test" {
  most_recent = true

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.test.id
  instance_type = "t3.micro"

  tags = {
    Name = "HelloWorld"
  }
}