from rest_framework import serializers
from myapp.models.agent import Agent
from myapp.models.department_agent import DepartmentAgent

class AgentSerializer(serializers.ModelSerializer):
    departments_count = serializers.SerializerMethodField()
    video_file_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Agent
        fields = ['id', 'agent_name', 'agent_short_desc', 'agent_long_desc', 
                 'problem', 'solution', 'video_file', 'video_file_url', 
                 'agent_configuration', 'agent_type', 'departments_count']
    
    def get_departments_count(self, obj):
        """Get the count of departments associated with this agent"""
        return DepartmentAgent.objects.filter(agent=obj).count()
    
    def get_video_file_url(self, obj):
        """Get the full URL for the video file"""
        if obj.video_file:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.video_file.url)
            return obj.video_file.url
        return None

class AgentListSerializer(serializers.ModelSerializer):
    """Simplified serializer for agent lists"""
    departments_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Agent
        fields = ['id', 'agent_name', 'agent_short_desc', 'agent_type', 'departments_count']
    
    def get_departments_count(self, obj):
        return DepartmentAgent.objects.filter(agent=obj).count()
