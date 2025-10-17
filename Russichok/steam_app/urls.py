from django.urls import path
from .views import *

urlpatterns = [
    path('', community_login),
]