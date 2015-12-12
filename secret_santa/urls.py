from django.conf.urls import url

from secret_santa import views

urlpatterns = [
    url(r'^$', views.home),
]
