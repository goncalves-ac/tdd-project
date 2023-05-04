from django.urls import re_path as url
from lists import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
]