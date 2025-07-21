from django.urls import path
from base import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('add/',views.add_task,name='add'),
    path('update_task/<int:pk>',views.update_task,name='update_task'),
    path('delete_task/<int:pk>',views.delete_,name='delete_task'),
]
