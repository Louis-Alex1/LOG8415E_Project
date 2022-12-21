# LOG8415E - Final Project
# infra.tf
# Terraform configuration relative to instance definitions

resource "aws_instance" "standalone" {
  count         = 1
  ami           = "ami-0574da719dca65348"
  instance_type = "t2.micro"
  associate_public_ip_address = true
  subnet_id              = aws_subnet.subnet1.id
}

resource "aws_instance" "cluster" {
  count         = 4
  ami           = "ami-0574da719dca65348"
  instance_type = "t2.micro"
  associate_public_ip_address = true
  subnet_id              = aws_subnet.subnet2.id
}