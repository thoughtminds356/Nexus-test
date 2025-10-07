import uuid
from django.db import models
from django.core.exceptions import ValidationError
import os

def validate_logo_file(value):
    """Validate that the uploaded file is a valid image or SVG"""
    if value:
        ext = os.path.splitext(value.name)[1].lower()
        valid_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp']
        if ext not in valid_extensions:
            raise ValidationError(f'Unsupported file extension. Allowed extensions: {", ".join(valid_extensions)}')
    return value

class Agent(models.Model):
    BOT = 'BOT'
    SITE = 'SITE'
    AGENT_TYPE_CHOICES = [
        (BOT, 'Bot'),
        (SITE, 'Site'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    agent_name = models.CharField(max_length=100)
    agent_short_desc = models.CharField(max_length=255)
    agent_long_desc = models.TextField(blank=True)
    problem = models.TextField(blank=True)
    solution = models.TextField(blank=True)
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    logo = models.FileField(upload_to='agent_logos/', blank=True, null=True, validators=[validate_logo_file])
    agent_configuration = models.JSONField(blank=True, null=True)
    agent_type = models.CharField(max_length=4, choices=AGENT_TYPE_CHOICES)

    def __str__(self):
        return self.agent_name
