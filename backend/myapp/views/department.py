from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from myapp.models.department import Department
from myapp.models.department_agent import DepartmentAgent
from myapp.serializers.department import DepartmentSerializer, DepartmentDetailSerializer
from myapp.serializers.agent import AgentListSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
    @action(detail=True, methods=['get'], url_path='agents')
    def get_agents(self, request, pk=None):
        """
        Get all agents associated with a specific department.
        URL: /departments/{department_id}/agents/
        """
        try:
            department = self.get_object()
            # Get all agents associated with this department through DepartmentAgent
            department_agents = DepartmentAgent.objects.filter(department=department).select_related('agent')
            agents = [da.agent for da in department_agents]
            
            serializer = AgentListSerializer(agents, many=True, context={'request': request})
            return Response({
                'department': DepartmentDetailSerializer(department).data,
                'agents': serializer.data,
                'total_agents': len(agents)
            }, status=status.HTTP_200_OK)
            
        except Department.DoesNotExist:
            return Response(
                {'error': 'Department not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
