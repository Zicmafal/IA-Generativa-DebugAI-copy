###############################################################
# MÓDULO EC2: Provisiona uma instância EC2 na AWS
###############################################################
resource "aws_instance" "main" {
  ami           = var.ami
  instance_type = var.instance_type
  subnet_id     = var.subnet_id
  vpc_security_group_ids = [var.security_group_id]

  # 🔹 Agora a instância recebe o par de chaves criado
  key_name = var.key_name

  user_data = var.user_data

  tags = {
    Name = var.name
  }
}
