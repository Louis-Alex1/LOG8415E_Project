# LOG8415E - Final Project
# infra.tf
# Terraform configuration relative to instance definitions

# Start one t2.large instance for the proxy
resource "aws_instance" "proxy" {
  count         = 1
  ami           = "ami-0a6b2839d44d781b2"
  instance_type = "t2.large"
  associate_public_ip_address = true
  user_data = templatefile("../scripts/proxy-config.sh.tftpl", {})
  subnet_id              = aws_subnet.subnet1.id
  key_name = "FinalProject"
  vpc_security_group_ids = [aws_security_group.proxy_security_group.id]
  tags = {
    Name = "proxy"
  }
}