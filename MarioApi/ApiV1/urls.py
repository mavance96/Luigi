from django.urls import path
from .endpoints.ConfigurationController import get_DevData
from .endpoints.BuildsController import queue_build, list_of_builds, getLastBuild
from .endpoints.ArtifactsController import get_ArtifactData
from .endpoints.ConfigurationController import getProjectsInOrganization
from .endpoints.PipelinesController import get_listOfPipelines
from .endpoints.AdminViewController import endpoint_driveTypes, endpoint_environments, endpoint_buildmaps

urlpatterns = [
    path('config/', get_DevData),
    path('queue/', queue_build),
    path('artifacts/', get_ArtifactData),
    path('projects/', getProjectsInOrganization),
    path('builds/', list_of_builds),
    path('pipelines/', get_listOfPipelines),
    path('lastBuild/', getLastBuild),
    path('drivetypes/', endpoint_driveTypes),
    path('environments/', endpoint_environments),
    path('buildmaps/', endpoint_buildmaps)
]
