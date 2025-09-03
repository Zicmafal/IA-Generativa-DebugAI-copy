###############################################################
# VARIÁVEIS DO MÓDULO EC2
# São preenchidas pelo root module (main.tf)
###############################################################
variable "ami" {}                # AMI da instância (imagem do SO)
variable "instance_type" {}      # Tipo da instância (ex: t3.micro)
variable "subnet_id" {}          # Subnet onde a instância será criada
variable "security_group_id" {}  # ID do Security Group associado
variable "key_name" {}           # Nome da chave SSH
variable "user_data" {}          # Script de inicialização
variable "name" {}               # Nome da instância
