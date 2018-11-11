from django.conf.urls import url

from . import views

app_name = 'inventory'

urlpatterns = [
    url(r'^(\d+)/$', views.inventory, name='index'),
    url(r'check-file/(\d+)/$', views.check_details, name='check-file'),
    url(r'upload-version/$', views.upload_version, name='upload-version'),
    url(r'ajax/update-version/$', views.update_version, name='update-version'),
]
