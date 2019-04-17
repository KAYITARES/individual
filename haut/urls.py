from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^mission',views.mission,name="mission"),
    url(r'^promoter',views.promoter,name="promoter"),
    url(r'^campuse',views.campuse,name="campuse"),
]