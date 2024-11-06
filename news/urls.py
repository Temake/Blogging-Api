from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('get-all-posts/',views.Getallpost),
    path('createposts/',views.addpost), 
    path('delete/',views.delete),
    path('update/',views.updatepost)
 
]