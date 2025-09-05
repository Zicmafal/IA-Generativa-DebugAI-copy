###############################################################
# MÓDULO EC2: Provisiona uma instância EC2 na AWS
###############################################################
resource "aws_instance" "main" {
  # AMI usada para criar a instância (ex: Ubuntu 22.04)
  ami           = var.ami

  # Tipo da instância (ex: t3.micro)
  instance_type = var.instance_type

  # Subnet onde a instância será provisionada
  subnet_id     = var.subnet_id

  # Security Group associado à instância
  vpc_security_group_ids = [var.security_group_id]

  # Par de chaves SSH criado no root module
  key_name = var.key_name

  # Script de inicialização (user_data)
  user_data = var.user_data

  # Tags para identificação da instância
  tags = {
    Name        = var.name
    Project     = "debugai"
    Environment = "dev"
    Owner       = "luiz"
  }
}
