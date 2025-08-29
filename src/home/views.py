from django.views.generic import TemplateView

__all__ = (
    'IndexView',
    'UserАgreementView',
)

class IndexView(TemplateView):
    template_name = 'home/index.html'


class UserАgreementView(TemplateView):
    template_name = 'home/user_agreement.html'
