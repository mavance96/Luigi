from django.urls import path
from .endpoints.ConfigurationController import get_DevData
from .endpoints.BuildsController import queue_build

urlpatterns = [
    path('config/', get_DevData),
    path('queue/', queue_build)
]