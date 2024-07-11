from django.urls import path, include
from board import views

urlpatterns = [
    path('', views.index, name='index'),
    path('board/<int:pk>',
         views.TopicListbyBoard.as_view(), name='topics-by-board'),
   
    ]