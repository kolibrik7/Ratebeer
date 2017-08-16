from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.zoznam, name="zoznam"),
	url(r'^pridanie_piva/$', views.pridanie_piva, name="pridanie_piva"),
	url(r'^editovanie_piva/(?P<beer_id>[0-9]+)/$', views.editovanie_piva, name="editovanie_piva"),
	url(r'^(?P<beer_id>[0-9]+)/$', views.detail, name="detail"),
]