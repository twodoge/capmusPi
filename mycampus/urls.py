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
	# url(r'^teasing/$', vs.teasing,name='teasing'),
	url(r'^send_teasing/$', vs.send_teasing,name='send_teasing'),
	url(r'^learn/$', vs.learn,name='learn'),
	url(r'^learn_refresh/$', vs.learn_refresh ,name='learn_refresh'),
	url(r'^send_learn/$', vs.send_learn,name='send_learn'),
	url(r'^forgotPassword/$', vs.forgotPassword,name='forgotPassword'),
	url(r'^setEmail/', vs.setEmail,name='setEmail'),
	url(r'^rePassword/$', vs.rePassword,name='rePassword'),
	url(r'^rePasswordSubmit/$', vs.rePasswordSubmit,name='rePasswordSubmit'),
	url(r'^content/$', vs.content,name='content'),
	url(r'^index1/$', vs.index1, name='index1'),
	url(r'^index_refresh/$', vs.index_refresh, name='index_refresh'),
	url(r'^test/$', vs.test , name='test'),
	url(r'^uploadImg/$', vs.uploadImg , name='uploadImg'),
	url(r'^content/(?P<new_id>[0-9]+)$', vs.content,name='content'),
	url(r'^comments_news/(?P<new_id>[0-9]+)$', vs.comments_news,name='comments_news'),
	url(r'^childcomments_news/(?P<comment_id>[0-9]+)$', vs.childcomments_news,name='childcomments_news'),
	url(r'^childcomments_learns/(?P<comment_id>[0-9]+)$', vs.childcomments_learns,name='childcomments_learns'),
	url(r'^content_learn/(?P<learn_id>[0-9]+)$', vs.content_learn,name='content_learn'),
	url(r'^user/$', vs.user,name='user'),
	url(r'^setting_information/$', vs.setting_information,name='setting_information'),
	url(r'^content_learn/(?P<new_id>[0-9]+)$', vs.content_learn,name='content_learn'),
	url(r'^cheack_name/$', vs.cheack_name ,name='cheack_name'),
	url(r'^change_user/$', vs.change_user ,name='change_user'),
	url(r'^comments_learn/(?P<learn_id>[0-9]+)$', vs.comments_learn,name='comments_learn'),
	url(r'^news_like_post/(?P<new_id>[0-9]+)$', vs.news_like_post,name='news_like_post'),
	url(r'^learns_like_post/(?P<learn_id>[0-9]+)$', vs.learns_like_post,name='learns_like_post'),
	url(r'^mypost/$', vs.mypost,name='mypost'),
	url(r'^delete_mynew/(?P<mynew_id>[0-9]+)$',vs.delete_mynew,name='delete_mynew'),
	url(r'^delete_mylearn/(?P<mylearn_id>[0-9]+)$',vs.delete_mylearn,name='delete_mylearn'),
	url(r'^search/$',vs.search,name='search'),
	url(r'login_out/$',vs.login_out ,name='login_out'),
	url(r'comment_child/$',vs.comment_child ,name='comment_child'),
]