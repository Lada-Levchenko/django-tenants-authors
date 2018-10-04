from django.contrib.auth.models import User
from django.views.generic import TemplateView

from customers.create_basic_tenants import create_tenants
from customers.models import Client


class TenantView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):

        context = super(TenantView, self).get_context_data(**kwargs)
        context['tenants_list'] = Client.objects.all()
        context['users'] = User.objects.all()
        return context
