from django.db import models

# Create your models here.
class User(models.Model):
	userName = models.CharField(max_length=20)
	userPicture = models.ImageField(upload_to='user_img',null=True)
	password = models.CharField(max_length=20)
	email = models.EmailField(max_length=30)
	phone = models.CharField(max_length=20)
	remark = models.CharField(max_length=30,null=True)

class News(models.Model):
	publisher = models.CharField(max_length=20)
	title = models.CharField(max_length=50,null=True)
	content = models.CharField(max_length=2000,null=True)
	images = models.ImageField(upload_to='news-img',null=True)
	time = models.DateTimeField(auto_now_add=True)
	likes = models.IntegerField(default=0,null=True)
	counts = models.IntegerField(default=0,null=True)
	uid = models.CharField(max_length=20)

class News_like(models.Model):
	critisID = models.CharField(max_length=20,null=True)
	new_id = models.IntegerField(null=True)
	liked = models.IntegerField(default=0)

class Comments_News(models.Model):
	critisID = models.CharField(max_length=20,null=True)
	new_id = models.IntegerField(null=True)
	time = models.DateTimeField(auto_now_add=True)
	content = models.CharField(max_length=255,null=True)
	images = models.ImageField(upload_to='news_img',null=True)

class Learns(models.Model):
	publisher = models.CharField(max_length=20)
	title = models.CharField(max_length=50)
	content = models.CharField(max_length=2000)
	images = models.ImageField(upload_to='learn_img',null=True)
	time = models.DateTimeField(auto_now_add=True)
	likes = models.IntegerField(default=0,null=True)
	counts = models.IntegerField(default=0,null=True)
	like = models.IntegerField(null=True)
	uid = models.CharField(max_length=20)

class Comments_Learns(models.Model):
	critisID = models.CharField(max_length=20)
	learn_id = models.IntegerField(null=True)
	time = models.DateTimeField(auto_now_add=True)
	content = models.CharField(max_length=255)
	images = models.ImageField(upload_to='learn_img',null=True)
	
class Lovewall(models.Model):
	publisher = models.CharField(max_length=20)
	tosb = models.CharField(max_length=50,null=True)
	content = models.CharField(max_length=2000,null=True)
	images = models.ImageField(upload_to='learn_img',null=True)
	time = models.DateTimeField(auto_now_add=True)
	fromsb = models.CharField(max_length=20)

class Comments_Lovewall(models.Model):
	critisID = models.IntegerField()
	time = models.DateTimeField(auto_now_add=True)
	content = models.CharField(max_length=255)

class Teasingwall(models.Model):
	publisher = models.CharField(max_length=20)
	content = models.CharField(max_length=2000)
	time = models.DateTimeField(auto_now_add=True)
	images = models.ImageField(upload_to='learn_img',null=True)
	tosb = models.CharField(max_length=50)
	fromsb = models.CharField(max_length=20)

class Comments_Teasingwall(models.Model):
	critisID = models.IntegerField()
	time = models.DateTimeField(auto_now_add=True)
	content = models.CharField(max_length=255)
