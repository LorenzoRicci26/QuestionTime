from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class IndexTemplateView(LoginRequiredMixin, TemplateView):
    """
    Render the index page.
    """
    template_name = 'index.html'