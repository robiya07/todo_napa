from django.db import models
from django.db.models import CharField, BooleanField, TextField


# Create your models here.


class TaskModel(models.Model):
    name = CharField(max_length=255)
    description = TextField()
    status = BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'