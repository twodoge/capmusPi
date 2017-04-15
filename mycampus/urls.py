from django.conf.urls import url
from mycampus import views as vs

urlpatterns = [
	url(r'^login/$', vs.login,name='login'),
	url(r'^index/$', vs.index,name='index'),
	url(r'^register/$', vs.register,name='register'),
	url(r'^register_action/', vs.register_action,name='register_action'),
	url(r'^loginJudge/', vs.loginJudge,name='loginJudge'),
	url(r'^check/', vs.check,name='check'),
	url(r'^member/$', vs.member,name='member'),
	url(r'^published/$', vs.published,name='published'),
	url(r'^show_published/$', vs.show_published,name='show_published'),
	url(r'^love/$', vs.love,name='love'),
	url(r'^send_love/$', vs.send_love,name='send_love'),
	url(r'^teasing/$', vs.teasing,name='teasing'),
	url(r'^send_teasing/$', vs.send_teasing,name='send_teasing'),
	url(r'^learn/$', vs.learn,name='learn'),
	url(r'^send_learn/$', vs.send_learn,name='send_learn'),
	url(r'^forgotPassword/$', vs.forgotPassword,name='forgotPassword'),
	url(r'^setEmail/', vs.setEmail,name='setEmail'),
	url(r'^rePassword/$', vs.rePassword,name='rePassword'),
	url(r'^rePasswordSubmit/$', vs.rePasswordSubmit,name='rePasswordSubmit'),
	url(r'^content/(?P<new_id>[0-9]+)$', vs.content,name='content'),
	url(r'^comments_news/(?P<new_id>[0-9]+)$', vs.comments_news,name='comments_news'),
	# url(r'^show_comments_news/$', vs.show_comments_news,name='show_comments_news'),

]