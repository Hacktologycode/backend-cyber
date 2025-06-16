from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)  # e.g., 'ESP32', 'Arduino', 'Pi'
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Session(models.Model):
    name = models.CharField(max_length=100)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class RedTeamAction(models.Model):
    ACTION_CHOICES = [
        ('port_scan', 'Port Scan'),
        ('brute_force', 'Brute Force'),
        ('ddos', 'DDoS'),
        ('mitm', 'MITM'),
        ('malware', 'Malware Injection'),
    ]
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=50, choices=ACTION_CHOICES)
    target_device = models.ForeignKey(Device, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    payload = models.TextField(blank=True)

class BlueTeamAction(models.Model):
    ACTION_CHOICES = [
        ('log_analysis', 'Log Analysis'),
        ('patch_applied', 'Patch Applied'),
        ('firewall_config', 'Firewall Config'),
        ('incident_response', 'Incident Response'),
    ]
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=50, choices=ACTION_CHOICES)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Alert(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    severity = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default="Unresolved")
    timestamp = models.DateTimeField(auto_now_add=True)
