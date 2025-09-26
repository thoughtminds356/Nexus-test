from rest_framework import serializers
from myapp.models.department_agent import DepartmentAgent

class DepartmentAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentAgent
        fields = '__all__'
