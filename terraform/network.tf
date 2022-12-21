# LOG8415E - Final Project
# network.tf
# Terraform configuration relative to network definitions

resource "aws_vpc" "my_vpc" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "subnet1" {
  vpc_id            = aws_vpc.my_vpc.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-east-1a"
}

resource "aws_network_interface" "interface1" {
  subnet_id   = aws_subnet.subnet1.id
  private_ips = ["10.0.1.1"]
}

resource "aws_subnet" "subnet2" {
  vpc_id            = aws_vpc.my_vpc.id
  cidr_block        = "10.0.2.0/24"
  availability_zone = "us-east-1a"
}

resource "aws_network_interface" "interface2" {
  subnet_id   = aws_subnet.subnet2.id
  private_ips = ["10.0.2.1", "10.0.2.2", "10.0.2.3", "10.0.2.4"]
}