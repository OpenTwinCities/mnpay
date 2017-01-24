from django.conf.urls import url

from . import views

app_name = "wages"
urlpatterns = [
    url(r'^wages$', views.get_wages, name='get_wages'),
    url(r'^wage_list$', views.get_wage_list, name='get_wage_list'),
    url(r'^limits$', views.get_limits, name='get_limits')
]
