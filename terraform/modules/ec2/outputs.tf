###############################################################
# OUTPUT DO MÓDULO EC2
# Retorna o IP público da instância criada
###############################################################
output "public_ip" {
  value = aws_instance.main.public_ip
}
