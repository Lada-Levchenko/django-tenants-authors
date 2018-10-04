from django.conf.urls import url
from django.contrib import admin

from blog.views import ArticleFormView, ArticlesView

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', ArticlesView.as_view(), name='article_list'),
    url(r'article/create/', ArticleFormView.as_view(), name='create_article')
]
