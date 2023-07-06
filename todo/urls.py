from django.urls import path

from todo.views import task_list_view, task_create_view, task_update_view, task_delete_view, task_detail_view

urlpatterns = [
    path('task/list', task_list_view, name='task_list'),
    path('task/create', task_create_view, name='task_create'),
    path('task/update/<int:pk>', task_update_view, name='task_update'),
    path('task/delete/<int:pk>', task_delete_view, name='task_delete'),
    path('task/detail/<int:pk>', task_detail_view, name='task_detail')
]
