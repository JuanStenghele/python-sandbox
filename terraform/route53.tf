resource "aws_route53_zone" "main" {
  name = var.main_domain_name
}

resource "aws_route53_record" "python_sandbox" {
  zone_id = aws_route53_zone.main.zone_id
  name    = "${var.python_sandbox_subdomain_name}.${var.main_domain_name}"
  type    = "CNAME"
  records = [data.kubernetes_service.python_sandbox_service.status[0].load_balancer[0].ingress[0].hostname]
  ttl     = 300
}

resource "aws_route53_record" "python_sandbox_www" {
  zone_id = aws_route53_zone.main.zone_id
  name    = "www.${var.python_sandbox_subdomain_name}.${var.main_domain_name}"
  type    = "CNAME"
  records = ["${var.python_sandbox_subdomain_name}.${var.main_domain_name}"]
  ttl     = 300
}
