from django.conf.urls import url, include
from rest_framework import routers
from wages import views

router = routers.DefaultRouter()
router.register(r'wages', views.WageViewSet)

app_name = "wages"
urlpatterns = [
    url(r'^', include(router.urls)),
]
