from django.db import models


class SmsVerification(models.Model):
    phone_number = models.CharField(max_length=16)
    verification_message = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.phone_number}, {self.verification_message}"
