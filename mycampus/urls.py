from django.conf.urls import url
from mycampus import views as vs

urlpatterns = [
	url(r'^login/$', vs.login,name='login'),
	url(r'^register/$', vs.register,name='register'),
	url(r'^index/$', vs.index,name='index'),
	url(r'^member/$', vs.member,name='member'),
	url(r'^published/$', vs.published,name='published'),
	url(r'^love/$', vs.love,name='love'),
	url(r'^learn/$', vs.learn,name='learn'),
]