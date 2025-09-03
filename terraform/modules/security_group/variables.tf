###############################################################
# VARIÁVEIS DO MÓDULO SECURITY GROUP
# São preenchidas pelo root module (main.tf)
###############################################################
variable "name" {}                # Nome do SG
variable "description" {}         # Descrição do SG
variable "vpc_id" {}              # VPC onde o SG será criado
variable "ingress_from_port" {}   # Porta inicial liberada
variable "ingress_to_port" {}     # Porta final liberada
