import uuid
from django.db import models
from .department import Department
from .agent import Agent

class DepartmentAgent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('department', 'agent')
