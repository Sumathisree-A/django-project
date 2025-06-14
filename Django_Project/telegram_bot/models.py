from django.db import models

class TelegramUser(models.Model):
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    chat_id = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.username
