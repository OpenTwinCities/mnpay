from django.conf.urls import url

from . import views

app_name = "wages"
urlpatterns = [
    url(r'^wages$', views.get_wages, name='get_wages'),
    url(r'^stats$', views.get_query_stats, name='get_stats'),
    url(r'^limits$', views.get_limits, name='get_limits')
]
