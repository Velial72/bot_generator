# bot_builder/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_bot_template, name='create_bot_template'),
    path('download/<int:bot_id>/', views.bot_download, name='bot_download'),
]