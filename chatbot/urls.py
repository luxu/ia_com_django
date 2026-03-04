from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot, name='chatbot'),
    path('list_models/', views.list_models, name='list_models'),
]
