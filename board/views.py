from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets, authentication, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import SprintSerializer, TaskSerializer, UserSerializer
from .models import Sprint, Task

from board.filter_class import TaskFilter
# Create your views here.

User = get_user_model()

class DefaultMixin(object):
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginated_by = 25
    paginate_by_param = 'page_size'
    max_paginate = 100
    filters_backends=(
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )




class SprintViewSet(DefaultMixin, viewsets.ModelViewSet):
    queryset = Sprint.objects.order_by('end')
    serializer_class = SprintSerializer
    search_fields = ('name',)
    ordering_fields = ('end', 'name', )


class TaskViewSet(DefaultMixin, viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_class = TaskFilter
    search_fields = ('name', 'description',)
    ordering_fields = ('name', 'order', 'started', 'due', 'completed', )

class UserViewSet(DefaultMixin, viewsets.ReadOnlyModelViewSet):
    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer
    search_fields = (User.USERNAME_FIELD)
