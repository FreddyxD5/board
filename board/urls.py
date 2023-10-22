from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('sprints', views.SprintViewSet, basename='sprint')
router.register('tasks', views.TaskViewSet, basename='tasks')
router.register('user', views.UserViewSet, basename='users')
