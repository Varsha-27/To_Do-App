from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('add_too',views.add_too,name='add_too'),
    path('delete_todo/<int:todo_id>/',views.delete_todo,name='delete_todo'),

    
    

]
