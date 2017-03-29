from django.conf.urls import url
from . import views
from django.views.generic import ListView, DetailView
from dojoteam.models import DojoMember, DojoMemberType

# This file is responsible for routing traffic in Django

#url(r'^$', ListView.as_view(queryset=DojoMember.objects.all(), template_name='dojoteam/dojoteam.html')),

# this is saying that from our dojoteam folder go to views.py and grab the Member function
# the name is important because is the name of the function in your view file for your app

urlpatterns = [
    url(r'^$', views.Member, name='Member'),
    url(r'^(?P<f_name>\w+)/$', views.memberClicked, name='memberClicked')
]
