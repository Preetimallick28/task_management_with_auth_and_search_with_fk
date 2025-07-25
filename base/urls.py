from django.urls import path
from base import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('add/',views.add_task,name='add'),
    path('update_task/<int:pk>',views.update_task,name='update_task'),
    path('confirm_delete/<int:pk>',views.confirm_delete,name='confirm_delete'),
    path('delete_/<int:pk>',views.delete_,name='delete_'),
    path('history',views.history,name='history'),
    path('delete_history/<int:pk>',views.delete_history,name='delete_history'),
    path('restore_history/<int:pk>',views.restore_history,name='restore_history'),
    path('clear_all',views.clear_all,name='clear_all'),
    path('restore_all',views.restore_all,name='restore_all'),
    
]
