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

class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    logo = models.FileField(upload_to='department_logos/', blank=True, null=True, validators=[validate_logo_file])

    def __str__(self):
        return self.name
