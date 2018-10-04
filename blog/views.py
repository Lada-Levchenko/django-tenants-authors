from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView
from blog.models import Article
from customers.create_basic_tenants import create_tenants
from customers.models import Client


class ArticleFormView(CreateView):

    model = Article
    template_name = 'article_form.html'
    fields = ['name', 'text']
    success_url = '/'

    def form_valid(self, form):
        Article.objects.create(author=self.request.tenant, **form.cleaned_data)
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super(ArticleFormView, self).get_context_data(**kwargs)
        context['tenants_list'] = Client.objects.all()
        context['current_tenant'] = self.request.tenant
        return context


class ArticlesView(ListView):
    template_name = 'articles.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticlesView, self).get_context_data(**kwargs)
        context['tenants_list'] = Client.objects.all()
        context['current_tenant'] = self.request.tenant
        return context
