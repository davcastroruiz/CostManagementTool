from django.conf.urls import url

from . import views

app_name = 'inventory'

urlpatterns = [
    url(r'^(\d+)/$', views.inventory, name='index'),
]
