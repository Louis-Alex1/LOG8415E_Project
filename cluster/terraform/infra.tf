# LOG8415E - Final Project
# infra.tf
# Terraform configuration relative to instance definitions

# Declaring 4 t2.micro instances for the cluster
resource "aws_instance" "cluster" {
  count         = 4
  ami           = "ami-0574da719dca65348"
  instance_type = "t2.micro"
  associate_public_ip_address = true
  subnet_id              = aws_subnet.subnet1.id
  key_name = "FinalProject"
  vpc_security_group_ids = [aws_security_group.ssh_mysql.id]
  tags = {
    Name = "cluster"
  }
}