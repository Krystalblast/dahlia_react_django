from django.urls import path
from . import views

app_name = "aupairnearby"

urlpatterns = [
    path('get_nearby/', views.get_nearby, name='get_nearby'),
    path('create_nearby/', views.create_nearby, name='create_nearby'),
    path('remove_nearby/', views.remove_nearby, name='remove_nearby'),
]
