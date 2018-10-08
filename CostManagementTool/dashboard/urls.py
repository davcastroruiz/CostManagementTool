from django.conf.urls import url

from . import views

app_name = 'dashboard'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'change-theme/(\d+)$', views.change_theme, name='change-theme'),
]