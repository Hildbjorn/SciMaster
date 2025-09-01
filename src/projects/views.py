from django.views.generic import TemplateView

__all__ = (
    'AllProjectsView',
    'ProjectDetailView',
)

class AllProjectsView(TemplateView):
    template_name = 'projects/all_projects.html'

class ProjectDetailView(TemplateView):
    template_name = 'projects/project_detail.html'