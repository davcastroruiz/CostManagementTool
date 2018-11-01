from django.conf.urls import url

from . import views

app_name = 'dashboard'

urlpatterns = [
    url(r'^$', views.dashboard, name='index'),
    url(r'change-theme/(\w+)$', views.change_theme, name='change-theme'),
    url(r'upload-file/$', views.update_details, name='upload-file'),
    url(r'save-project/$', views.save_project, name='save-project'),
    url(r'remove-project/$', views.remove_project, name='remove-project'),
]