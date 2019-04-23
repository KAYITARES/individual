from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^mission',views.mission,name="mission"),
    url(r'^promoter',views.promoter,name="promoter"),
    url(r'^campuse',views.campuse,name="campuse"),
    url(r'^image',views.image,name="image"),
    url(r'^staff',views.staff,name="staff"),
    url(r'^registration',views.registration,name="registration"),
  
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)