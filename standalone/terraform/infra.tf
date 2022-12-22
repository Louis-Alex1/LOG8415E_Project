# LOG8415E - Final Project
# infra.tf
# Terraform configuration relative to instance definitions

# Start one t2.micro instance for the standalone
resource "aws_instance" "standalone" {
  count         = 1
  ami           = "ami-0574da719dca65348"
  instance_type = "t2.micro"
  associate_public_ip_address = true
  user_data = templatefile("../scripts/standalone-config.sh.tftpl", {
    number = count.index
  })
  subnet_id              = aws_subnet.subnet1.id
  key_name = "FinalProject"
  vpc_security_group_ids = [aws_security_group.ssh_mysql.id]
  tags = {
    Name = "standalone"
  }
}