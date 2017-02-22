from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^dashboard/$', views.dash, name = "dash"),
	url(r'^item/$', views.item, name = "item"),
        url(r'^vendor/$', views.vendor, name = "vendor"),
        

]
