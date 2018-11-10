from django.conf.urls import url

from . import views

app_name = 'dashboard'

urlpatterns = [
    url(r'^$', views.dashboard, name='index'),
    url(r'change-theme/(\w+)$', views.change_theme, name='change-theme'),
    url(r'admin-fields/$', views.fields, name='admin-fields'),
    url(r'save-project/$', views.save_project, name='save-project'),
    url(r'save-field/$', views.save_field, name='save-field'),
    url(r'assign-fields/$', views.assign_fields, name='assign-fields'),
    url(r'remove-project/$', views.remove_project, name='remove-project'),
    url(r'remove-field/$', views.remove_field, name='remove-field'),
]
