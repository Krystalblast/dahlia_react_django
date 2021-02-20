from django.urls import path
from django.conf.urls import url
from rest_framework.authtoken import views
from .views import *

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    #url(r'^signout/$', SignOutView.as_view(), name=r"signout"),
    path('signout/', SignOutView.as_view(),name='signout'),
    path('update_profile/', ProfileUpdateView.as_view(),name='update_profile'),
   # path('token/', views.obtain_auth_token),
]