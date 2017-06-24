from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^channels$', views.channel_list),
    url(r'^categories$', views.category_list),
]