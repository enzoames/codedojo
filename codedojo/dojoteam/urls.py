from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from dojoteam.models import DojoMember, DojoMemberType

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=DojoMember.objects.all(), template_name='dojoteam/dojoteam.html')),
    # url((r'(?P)')
]