#coding:utf-8
from django.shortcuts import render, render_to_response, HttpResponse, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from . import models
import string, os, random
from PIL import Image, ImageDraw, ImageFont 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def login(request):
    return render(request, 'campus/login.html')
def test(request):
    return render(request, 'campus/test.html')

def  register(request):
	return render(request, 'campus/register.html')

def register_action(request):
	if request.is_ajax():
		Name = request.GET.get('Name')
		user = models.User.objects.filter(userName=Name)
		if user:
			error = "该用户已存在"
			r = HttpResponse(error)
			return r
		else:
			error = ""
			r = HttpResponse(error)
			return r 
        
	else:
		userName = request.POST.get('userName')
		password =request.POST.get('password')
		email = request.POST.get('email')
		phone =request.POST.get('phone')
		models.User.objects.create(userName=userName,password=password,email=email,phone=phone)
		return redirect('/mycampus/login/')
        


def loginJudge(request):
	if request.is_ajax():
		userName = request.GET.get('userName')
		password = request.GET.get('password')
		user = models.User.objects.filter(userName=userName)
		print (user)
		if len(user)==0:
			error = "该用户不存在"
			r = HttpResponse(error)
			return r
		else:
			if user[0]:
				if user[0].password==password:
					error = ""
					r = HttpResponse(error)
					request.session['userId'] = user[0].id
					return r 
				else:
					error = "用户名或密码不正确"
					r = HttpResponse(error)
					return r
				error = "该用户不存在"
				r = HttpResponse(error)
				return r
			else:
				error = "该用户不存在"
				r = HttpResponse(error)
				return r
#主页	
def index(request):
	userId = request.session.get('userId',default=None)
	user = models.User.objects.get(pk=userId)
	news = models.News.objects.order_by('-id')
	return render(request, 'campus/index.html',{'news':news,'user':user})
	
def index1(request):
	return render(request, 'campus/index1.html')

def member(request):
	userId = request.session.get('userId',default=None)
	user = models.User.objects.get(pk=userId)
	return render(request, 'campus/member.html',{'user':user})
	news = models.News.objects.order_by('-id')
	return render(request, 'campus/index.html',{'news':news})
#详细内容页面
def content(request,new_id):
	# request.session['new_id'] = new_id
	news =models.News.objects.get(pk=new_id)
	comments = models.Comments_News.objects.filter(new_id=new_id)
	return render(request, 'campus/content.html',{'news':news,'comments':comments})
#发表新闻评论
def comments_news(request,new_id):
	news =models.News.objects.get(pk=new_id)
	userId = request.session.get('userId',default=None)
	user = models.User.objects.get(pk=userId)
	content = request.POST.get('content','content')
	images = request.FILES.get('image')
	models.Comments_News.objects.create(critisID=user.userName,content=content,images=images,new_id=news.id)
	news.counts = news.counts+1
	news.save()
	comments = models.Comments_News.objects.filter(new_id=new_id)
	return render(request, 'campus/content.html',{'news':news,'comments':comments})
#点赞
def like_post(request,new_id):
	userId = request.session.get('userId',default=None)
	user = models.User.objects.get(pk=userId)
	news = models.News.objects.get(pk=new_id)
	like = models.News_like.objects.filter(new=new_id)
	# 取消点赞
	if(like):
		if(like[0].liked==1):
			news.likes-=1
			news.save()
			models.News_like.objects.filter(new=new_id).update(liked=0)
		else:
			news.likes+=1
			news.save()
			models.News_like.objects.filter(new=new_id).update(liked=1)
	else:
		news.likes+=1
		news.save()
		models.News_like.objects.create(critis=user,new=news,liked=1)
	comments = models.Comments_News.objects.filter(new_id=new_id)
	news = models.News.objects.get(pk=new_id)
	return render(request, 'campus/content.html',{'news':news,'comments':comments})

#学习详情
def content_learn(request,learn_id):
	# request.session['new_id'] = new_id
	learns =models.Learns.objects.get(pk=learn_id)
	comments = models.Comments_Learns.objects.filter(learn_id=learn_id)
	return render(request, 'campus/content_learn.html',{'learns':learns,'comments':comments})
#评论学习
def comments_learn(request,learn_id):
	learns =models.Learns.objects.get(pk=learn_id)
	userId = request.session.get('userId',default=None)
	user = models.User.objects.get(pk=userId)
	content = request.POST.get('content','content')
	images = request.FILES.get('image')
	models.Comments_Learns.objects.create(critisID=user.userName,content=content,images=images,learn_id=learns.id)
	comments = models.Comments_Learns.objects.filter(learn_id=learn_id)
	return render(request, 'campus/content_learn.html',{'learns':learns,'comments':comments})
#发表新闻事件
def show_published(request):
	userId = request.session.get('userId',default=None)
	user = models.User.objects.get(pk=userId)
	title = request.POST.get('title','title')
	content = request.POST.get('content','content')
	images = request.FILES.get('image')
	models.News.objects.create(publisher=user.userName,title=title,content=content,images=images)
	return redirect('/mycampus/index')
	
def published(request):
	return render(request, 'campus/published.html')
#显示表白墙
def love(request):
	loves = models.Lovewall.objects.order_by('-id')
	teasings = models.Teasingwall.objects.order_by('-id')
	return render(request, 'campus/love.html',{'loves':loves,'teasings':teasings})
#发送表白信息
def send_love(request):
	userId = request.session.get('userId',default=None)
	user = models.User.objects.get(pk=userId)
	tosb = request.POST.get('tosb','tosb')
	content = request.POST.get('content','content')
	image = request.FILES.get('image')
	fromsb = request.POST.get('fromsb','fromsb')
	if fromsb=='':
		fromsb='匿名用户'
	models.Lovewall.objects.create(publisher=user.userName,tosb=tosb,content=content,images=image,fromsb=fromsb)
	return redirect('/mycampus/love')
#显示吐槽墙
def teasing(request):
 	teasings = models.Teasingwall.objects.order_by('-id')
 	return render(request, 'campus/love.html',{'teasings':teasings})
#发送吐槽信息
def send_teasing(request):
	userId = request.session.get('userId',default=None)
	user = models.User.objects.get(pk=userId)
	tosb = request.POST.get('tosb','tosb')
	content = request.POST.get('content','content')
	image = request.FILES.get('image')
	fromsb = request.POST.get('fromsb','fromsb')
	if fromsb=='':
		fromsb='匿名用户'
	models.Teasingwall.objects.create(publisher=user.userName,tosb=tosb,content=content,images=image,fromsb=fromsb)
	return redirect('/mycampus/love')
	return render(request, 'campus/love.html')
#研讨天地页面
def learn(request):
	learns = models.Learns.objects.order_by('-id')
	return render(request, 'campus/learn.html',{'learns':learns})
#发表研讨事件
def send_learn(request):
	userId = request.session.get('userId',default=None)
	user = models.User.objects.get(pk=userId)
	title = request.POST.get('title','title')
	content = request.POST.get('content','content')
	image = request.FILES.get('image')
	models.Learns.objects.create(publisher=user.userName,title=title,content=content,images=image)
	return redirect('/mycampus/learn')
	
def forgotPassword(request):
	return render(request, 'campus/forgotPassword.html')

#发送邮件
def setEmail(request):
	if request.is_ajax():
		email = request.GET.get('email', '')
		print(email+"1334485787")
		user = models.User.objects.filter(email=email)
		if user:
			request.session['userName'] = user[0].userName
			check = ""
			i = 0
			while i<4:
				check+=str(random.randint(0,9))
				i=i+1
			request.session['check'] = check
			subject = '请重置您的密码'
			text_content = '请重置您的密码'
			html_content = '您的验证码为:'+check
			msg = EmailMultiAlternatives(subject, text_content, '2384236461@qq.com', [email])
			msg.attach_alternative(html_content, "text/html")
			msg.send()
			error = ""
			r = HttpResponse(error)
			return r
		else:
			error = "该邮箱不存在，请前往注册"
			r = HttpResponse(error)
			return r

def check(request):
	if request.is_ajax():
		email = request.GET.get('email', '')
		checkcode = request.GET.get('checkcode', '')
		print(email+checkcode)
		user = models.User.objects.filter(email=email)
		if user:
			check = request.session.get('check')
			if checkcode == check:
				error = ""
				r = HttpResponse(error)
				return r
			else:
				error = "验证码错误"
				r = HttpResponse(error)
				return r
		else:
			error = "该邮箱不存在"
			r = HttpResponse
			return r

# 重置密码页面	
def rePassword(request):
	return render(request, 'campus/rePassword.html')

def rePasswordSubmit(request):
	userName=request.session.get('userName',default=None)
	print(userName)
	user = models.User.objects.get(userName=userName)
	print(user.password)
	password = request.POST.get('password', '')
	print(password)
	user.password = password
	user.save()
	return redirect('/mycampus/login/')


#修改头像
def uploadImg(request):
	userId = request.session.get('userId',default=None)
	user = models.User.objects.get(pk=userId)
	image = request.FILES.get('image')
	user.userPicture = image
	print (user.userPicture)
	user.save()
	return redirect('/mycampus/member')
