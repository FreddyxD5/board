import django_filters
from django.contrib.auth import get_user_model
from .models import Task


User = get_user_model()

class NullFilter(django_filters.BooleanFilter):
    """ Filtro en un conjunto de campos como nulos o no"""

    def filter(self, qs, value):
        if value is not None:
            return qs.filter(**{'%s__isnull'% self.name:value})
        return qs
    

class TaskFilter(django_filters.FilterSet):
    backlog = NullFilter(name="sprint")
    class Meta:
        model = Task 
        fields = ('sprint', 'status', 'assigned', 'backlog', )
