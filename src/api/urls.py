from rest_framework.routers import DefaultRouter
from api.views.user_app import UserModeViewSet
from django.urls import path, include

r = DefaultRouter()

r.register(r'users', UserModeViewSet, basename='users')

urlpatterens = [
    path('', include(r.urls)),
]