from rest_framework import viewsets
from myapp.models.department_agent import DepartmentAgent
from myapp.serializers.department_agent import DepartmentAgentSerializer

class DepartmentAgentViewSet(viewsets.ModelViewSet):
    queryset = DepartmentAgent.objects.all()
    serializer_class = DepartmentAgentSerializer
