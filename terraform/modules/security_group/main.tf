###############################################################
# MÓDULO SECURITY GROUP: Cria um SG para liberar portas
###############################################################
resource "aws_security_group" "main" {
  name        = var.name           # Nome do SG
  description = var.description    # Descrição do SG
  vpc_id      = var.vpc_id         # VPC onde o SG será criado

  ingress {
    from_port   = var.ingress_from_port # Porta inicial liberada
    to_port     = var.ingress_to_port   # Porta final liberada
    protocol    = "tcp"                # Protocolo TCP
    cidr_blocks = ["0.0.0.0/0"]        # Acesso liberado para todos
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]        # Saída liberada para todos
  }

  tags = {
    Name = var.name                  # Nome para identificação
  }
}
