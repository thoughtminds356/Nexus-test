from rest_framework import serializers
from myapp.models.department import Department
from myapp.models.department_agent import DepartmentAgent

class DepartmentSerializer(serializers.ModelSerializer):
    agents_count = serializers.SerializerMethodField()
    logo_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Department
        fields = ['id', 'name', 'logo', 'logo_url', 'agents_count']
    
    def get_agents_count(self, obj):
        """Get the count of agents associated with this department"""
        return DepartmentAgent.objects.filter(department=obj).count()
    
    def get_logo_url(self, obj):
        """Get the full URL for the logo image"""
        if obj.logo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.logo.url)
            return obj.logo.url
        return None

class DepartmentDetailSerializer(serializers.ModelSerializer):
    """Detailed serializer for department with all information"""
    class Meta:
        model = Department
        fields = '__all__'
