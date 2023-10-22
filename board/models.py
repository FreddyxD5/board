from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Sprint(models.Model):
    name = models.CharField(_("Nombre del sprint"), max_length=100, blank=True, default='')
    description = models.TextField(_("Descripcion del sprint"), blank=True, default='')
    end = models.DateField(_("Fin del Sprint"), unique=True)

    def __str__(self):
        return self.name or _('Sprint ending %s'), self.end



class Task(models.Model):
    STATUS_TODO = 1
    STATUS_IN_PROGRESS = 2
    STATUS_TESTING = 3
    STATUS_DONE = 4

    STATUS_CHOICES = (
        (STATUS_TODO,_('Not Started')),
        (STATUS_IN_PROGRESS,_('In Progress')),
        (STATUS_TESTING,_('Testing')),
        (STATUS_DONE,_('Done')),
    )

    name = models.CharField(_("Nombre de la Tarea"), max_length=100)
    description = models.TextField(_("Descripcion de la tarea"), blank=True, default='')
    sprint = models.ForeignKey(Sprint, blank=True, null=True, on_delete=models.CASCADE)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=STATUS_TODO)
    order = models.SmallIntegerField(default=0)
    assigned = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, on_delete=models.DO_NOTHING)
    started = models.DateField(blank=True, null=True)
    due = models.DateField(blank=True, null=True)
    completed = models.DateField(blank=True, null=True)

    def __str_(self):    
        return self.name
    