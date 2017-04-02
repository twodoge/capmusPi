from django.db import models

# Create your models here.
class User(models.Model):
	userName = models.CharField(max_length=20)
	userPicture = models.ImageField(upload_to='img',null=True)
	password = models.CharField(max_length=20)
	email = models.EmailField(max_length=30)
	phone = models.CharField(max_length=20)
	remark = models.CharField(max_length=30,null=True)
