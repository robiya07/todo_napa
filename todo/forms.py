from django.forms import ModelForm

from todo.models import TaskModel


class TaskCreateModelForm(ModelForm):
    class Meta:
        model = TaskModel
        fields = ('name', 'description')


class TaskUpdateModelForm(ModelForm):
    class Meta:
        model = TaskModel
        exclude = ('created_at',)
