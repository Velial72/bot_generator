# bot_generator/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bot_builder/', include('bot_builder.urls')),
]