from django.contrib import admin

# Register your models here.
from mycampus.models import User
from mycampus.models import News
from mycampus.models import News_like
from mycampus.models import Comments_News
from mycampus.models import ChildComments_News
from mycampus.models import Learns
from mycampus.models import Comments_Learns
from mycampus.models import ChildComments_Learns
from mycampus.models import Learns_like
from mycampus.models import Lovewall
from mycampus.models import Comments_Lovewall
from mycampus.models import Teasingwall
from mycampus.models import Comments_Teasingwall

class Useradmin(admin.ModelAdmin):
	list_display=('userName','password','email','phone','remark')

class Newsadmin(admin.ModelAdmin):
	list_display=('publisher','title','time','likes','counts')
	list_filter =('time',)

class News_likeadmin(admin.ModelAdmin):
	list_display=('critisID','new_id','liked')

class Comments_Newsadmin(admin.ModelAdmin):
	list_display=('critisID','new_id','time','content')
	list_filter =('time',)

class ChildComments_Newsadmin(admin.ModelAdmin):
	list_display=('critisID','new_id','time','content')
	list_filter =('time',)

class Learnsadmin(admin.ModelAdmin):
	list_display=('publisher','title','content','time','likes')
	list_filter =('time',)

class Comments_Learnsadmin(admin.ModelAdmin):
	list_display=('critisID','learn_id','time','content')
	list_filter =('time',)

class ChildComments_Learnsadmin(admin.ModelAdmin):
	list_display=('critisID','learn_id','time','content')
	list_filter =('time',)

class Learns_likeadmin(admin.ModelAdmin):
	list_display=('critisID','learn_id','liked')

class Lovewalladmin(admin.ModelAdmin):
	list_display=('publisher','content','time','tosb','fromsb')
	list_filter =('time',)

class Comments_Lovewalladmin(admin.ModelAdmin):
	list_display=('critisID','time','content')
	list_filter =('time',)

class Teasingwalladmin(admin.ModelAdmin):
	list_display=('publisher','content','time','tosb','fromsb')
	list_filter =('time',)

class Comments_Teasingwalladmin(admin.ModelAdmin):
	list_display=('critisID','time','content')
	list_filter =('time',)

admin.site.register(User,Useradmin)
admin.site.register(News,Newsadmin)
admin.site.register(News_like,News_likeadmin)
admin.site.register(Comments_News,Comments_Newsadmin)
admin.site.register(ChildComments_News,ChildComments_Newsadmin)
admin.site.register(Learns,Learnsadmin)
admin.site.register(Comments_Learns,Comments_Learnsadmin)
admin.site.register(ChildComments_Learns,ChildComments_Learnsadmin)
admin.site.register(Learns_like,Learns_likeadmin)
admin.site.register(Lovewall,Lovewalladmin)
admin.site.register(Comments_Lovewall,Comments_Lovewalladmin)
admin.site.register(Teasingwall,Teasingwalladmin)
admin.site.register(Comments_Teasingwall,Comments_Teasingwalladmin)
