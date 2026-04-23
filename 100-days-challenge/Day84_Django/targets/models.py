from django.db import models

class Target(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name="Target IP")
    hostname = models.CharField(max_length=200, blank=True, null=True)
    open_ports = models.CharField(max_length=200, blank=True)
    vulnerability_status = models.CharField(
        max_length=20,
        choices=[('Clean', 'Clean'), ('Vulnerable', 'Vulnerable'), ('Exploited', 'Exploited')],
        default='Clean'
    )
    notes = models.TextField(blank=True)
    discovered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} - [{self.vulnerability_status}]"