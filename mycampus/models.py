from django.db import models

# Create your models here.
class User(models.Model):
	userName = models.CharField(max_length=20)
	userPicture = models.ImageField(upload_to='img',null=True)
	password = models.CharField(max_length=20)
	email = models.EmailField(max_length=30)
	phone = models.CharField(max_length=20)
	remark = models.CharField(max_length=30,null=True)

class News(models.Model):
	publisher = models.CharField(max_length=20)
	title = models.CharField(max_length=50)
	content = models.CharField(max_length=2000)
	images = models.ImageField(upload_to='news-img',null=True)
	time = models.DateTimeField(auto_now_add=True)
	like = models.IntegerField()

class Comments_News(models.Model):
	critisID = models.IntegerField()
	time = models.DateTimeField(auto_now_add=True)
	content = models.CharField(max_length=255)

class Learns(models.Model):
	publisher = models.CharField(max_length=20)
	title = models.CharField(max_length=50)
	content = models.CharField(max_length=2000)
	images = models.ImageField(upload_to='news-img',null=True)
	time = models.DateTimeField(auto_now_add=True)
	like = models.IntegerField()

class Comments_Learns(models.Model):
	critisID = models.IntegerField()
	time = models.DateTimeField(auto_now_add=True)
	content = models.CharField(max_length=255)

class Lovewall(models.Model):
	publisher = models.CharField(max_length=20)
	content = models.CharField(max_length=2000)
	time = models.DateTimeField(auto_now_add=True)

class Comments_Lovewall(models.Model):
	critisID = models.IntegerField()
	time = models.DateTimeField(auto_now_add=True)
	content = models.CharField(max_length=255)

class Teasingwall(models.Model):
	publisher = models.CharField(max_length=20)
	content = models.CharField(max_length=2000)
	time = models.DateTimeField(auto_now_add=True)

class Comments_Teasingwall(models.Model):
	critisID = models.IntegerField()
	time = models.DateTimeField(auto_now_add=True)
	content = models.CharField(max_length=255)
