from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^wages$', views.get_wages, name='get_wages'),
]
