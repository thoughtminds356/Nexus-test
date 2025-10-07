from rest_framework import serializers
from myapp.models.department import Department
from myapp.models.department_agent import DepartmentAgent

class DepartmentSerializer(serializers.ModelSerializer):
    agents_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Department
        fields = ['id', 'name', 'agents_count']
    
    def get_agents_count(self, obj):
        """Get the count of agents associated with this department"""
        return DepartmentAgent.objects.filter(department=obj).count()

class DepartmentDetailSerializer(serializers.ModelSerializer):
    """Detailed serializer for department with all information"""
    class Meta:
        model = Department
        fields = '__all__'
