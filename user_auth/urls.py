from django.urls import path
from user_auth import views

urlpatterns = [
    path('',views.login_,name='login'),
    path('register/',views.register_,name='register'),
    path('logout/',views.logout_,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('update_profile',views.update_profile,name='update_profile'),
    path('change_pass',views.change_pass,name='change_pass'),
]
