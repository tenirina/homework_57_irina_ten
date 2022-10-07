from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from webapp.models import Issue


class IssueView(TemplateView):
    template_name = 'issue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['issue'] = get_object_or_404(Issue, pk=kwargs['pk'])
        return context


class AddView(TemplateView):
    template_name = 'add.html'