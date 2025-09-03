###############################################################
# OUTPUT DO MÓDULO SECURITY GROUP
# Retorna o ID do SG criado para ser usado em outros módulos
###############################################################
output "security_group_id" {
  value = aws_security_group.main.id
}
