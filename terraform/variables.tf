variable "app_name" {
  description = "Application Name"
  type        = string
  default     = "juans-python-sandbox"
}

variable "aws_region" {
  description = "AWS Region"
  type        = string
  default     = "sa-east-1"
}

variable "main_domain_name" {
  description = "Kubernetes app domain name"
  type        = string
  default     = "25101999.xyz"
}

variable "python_sandbox_subdomain_name" {
  description = "Subdomain for the python-sandbox service"
  type        = string
  default     = "python-sandbox"
}
