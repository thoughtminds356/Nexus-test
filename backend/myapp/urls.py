from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import AgentViewSet, DepartmentViewSet, DepartmentAgentViewSet

router = DefaultRouter()
router.register(r'agents', AgentViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'department-agents', DepartmentAgentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
