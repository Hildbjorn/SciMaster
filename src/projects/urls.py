from django.urls import path
from .views import *

urlpatterns = [
    path('all_projects', AllProjectsView.as_view(), name='all_projects'),
    path('project_detail', ProjectDetailView.as_view(), name='project_detail'),
]
