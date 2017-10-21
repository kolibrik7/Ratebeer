from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.zoznam, name="zoznam"),
	url(r'^pridanie_hodnotenia/$', views.pridanie_hodnotenia, name="pridanie_hodnotenia"),
	url(r'^(?P<rating_id>[0-9]+)/$', views.detail, name="detail"),
	url(r'^(?P<rating_id>[0-9]+)/uprava_hodnotenia/$', views.uprava_hodnotenia, name="uprava_hodnotenia"),
	url(r'^(?P<rating_id>[0-9]+)/zmazanie_hodnotenia_a77K5YhrT1X0HUBVopWs/$', views.zmazanie_hodnotenia, name="zmazanie_hodnotenia"),
	url(r'^ajax/pivovar_atributy/$', views.pivovar_atributy, name="pivovar_atributy"),
	url(r'^ajax/pivo_atributy/$', views.pivo_atributy, name="pivo_atributy"),
]