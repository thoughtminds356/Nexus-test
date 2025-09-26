from rest_framework import viewsets
from myapp.models.agent import Agent
from myapp.serializers.agent import AgentSerializer

class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
