from rest_framework import viewsets
from myapp.models.department import Department
from myapp.serializers.department import DepartmentSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
