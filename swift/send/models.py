from django.db import models

class SendMail(models.Model):
    name = models.CharField(max_length=120, default='')
    subject = models.CharField(max_length=120, default='')
    to = models.EmailField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.subject}'