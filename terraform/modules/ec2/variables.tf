###############################################################
# VARIÁVEIS DO MÓDULO EC2
# São preenchidas pelo root module (main.tf)
###############################################################

variable "ami" {
  description = "AMI da instância (imagem do SO, ex: Ubuntu 22.04)"
  type        = string
}

variable "instance_type" {
  description = "Tipo da instância EC2 (ex: t3.micro)"
  type        = string
}

variable "subnet_id" {
  description = "Subnet ID onde a instância será criada"
  type        = string
}

variable "security_group_id" {
  description = "ID do Security Group associado à instância"
  type        = string
}

variable "key_name" {
  description = "Nome do par de chaves SSH para acessar a instância"
  type        = string
}

variable "user_data" {
  description = "Script de inicialização da instância (user_data)"
  type        = string
  default     = ""   # Permite que seja opcional
}

variable "name" {
  description = "Nome da instância (tag Name)"
  type        = string
}
