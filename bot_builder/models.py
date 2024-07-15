# bot_builder/models.py
from django.db import models

class BotTemplate(models.Model):
    name = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    start_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
