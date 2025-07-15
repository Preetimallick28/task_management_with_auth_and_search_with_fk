from django.urls import path
from user_auth import views

urlpatterns = [
    path('',views.login_,name='login'),
    path('register/',views.register_,name='register'),
]
