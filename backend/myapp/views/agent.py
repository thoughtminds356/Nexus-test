from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from myapp.models.agent import Agent
from myapp.models.department_agent import DepartmentAgent
from myapp.serializers.agent import AgentSerializer
from myapp.serializers.department import DepartmentSerializer

class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    
    def retrieve(self, request, pk=None):
        """
        Get detailed information about a specific agent including associated departments.
        URL: /agents/{agent_id}/
        """
        try:
            agent = self.get_object()
            # Get all departments associated with this agent
            department_agents = DepartmentAgent.objects.filter(agent=agent).select_related('department')
            departments = [da.department for da in department_agents]
            
            agent_data = AgentSerializer(agent, context={'request': request}).data
            departments_data = DepartmentSerializer(departments, many=True).data
            
            return Response({
                'agent': agent_data,
                'departments': departments_data,
                'total_departments': len(departments)
            }, status=status.HTTP_200_OK)
            
        except Agent.DoesNotExist:
            return Response(
                {'error': 'Agent not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
    
    @action(detail=True, methods=['get'], url_path='departments')
    def get_departments(self, request, pk=None):
        """
        Get all departments associated with a specific agent.
        URL: /agents/{agent_id}/departments/
        """
        try:
            agent = self.get_object()
            department_agents = DepartmentAgent.objects.filter(agent=agent).select_related('department')
            departments = [da.department for da in department_agents]
            
            serializer = DepartmentSerializer(departments, many=True)
            return Response({
                'agent': AgentSerializer(agent, context={'request': request}).data,
                'departments': serializer.data,
                'total_departments': len(departments)
            }, status=status.HTTP_200_OK)
            
        except Agent.DoesNotExist:
            return Response(
                {'error': 'Agent not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
