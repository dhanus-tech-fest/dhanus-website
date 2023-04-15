from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255)
    is_active = models.CharField(max_length=10)
    contact = models.CharField(max_length=255)
    description = models.TextField()
    prize = models.TextField()
    guidelines = models.TextField()
    konf_hub_url = models.TextField()
    image = models.ImageField(upload_to='event_images/')
