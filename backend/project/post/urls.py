from . import views
from rest_framework.routers import SimpleRouter

routers = SimpleRouter()
routers.register("posts", views.PostViewSet, "posts")

urlpatterns = routers.urls