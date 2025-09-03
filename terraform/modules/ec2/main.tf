###############################################################
# MÓDULO EC2: Provisiona uma instância EC2 na AWS
###############################################################
resource "aws_instance" "main" {
  ami           = var.ami                 # AMI da instância (imagem do SO)
  instance_type = var.instance_type       # Tipo da instância (ex: t3.micro)
  subnet_id     = var.subnet_id           # Subnet onde a instância será criada
  vpc_security_group_ids = [var.security_group_id] # Security Group associado
  key_name      = var.key_name            # Chave SSH para acesso

  user_data = var.user_data               # Script de inicialização (instala Docker, clona projeto, etc)

  tags = {
    Name = var.name                       # Nome da instância para identificação
  }
}
