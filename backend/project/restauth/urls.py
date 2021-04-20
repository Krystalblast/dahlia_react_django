from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', SignOutView.as_view(), name='signout'),
    path('update_profile/', ProfileUpdateView.as_view(), name='update_profile'),
    path('get_user/', get_user, name='get_user'),
    path('get_profile/', get_profile, name='get_profile'),
]
