from django.urls import path
from . import views
from .views import GroupsView

app_name = "group"

urlpatterns = [
    path('get_groups/<int:user_id>', GroupsView.get_groups, name='get_groups'),
    path('create_group/', views.create_group, name='create_group'),
    path('remove_group/', views.remove_group, name='remove_group'),
]
