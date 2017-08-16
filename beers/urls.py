from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.zoznam, name="zoznam"),
	url(r'^pridanie_hodnotenia/$', views.pridanie_hodnotenia, name="pridanie_hodnotenia"),
	url(r'^(?P<rating_id>[0-9]+)/$', views.detail, name="detail"),
	url(r'^(?P<rating_id>[0-9]+)/uprava_hodnotenia/$', views.uprava_hodnotenia, name="uprava_hodnotenia"),
]