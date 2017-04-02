#coding:utf-8
from django.shortcuts import render, render_to_response, HttpResponse, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from . import models
def login(request):
    return render(request, 'campus/login.html')

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
		if user:
			if user[0].password==password:

				error = ""
				r = HttpResponse(error)
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
	
def index(request):
	return render(request,'campus/index.html')

def  member(request):
	return render(request, 'campus/member.html')
	
def  published(request):
	return render(request, 'campus/published.html')

def love(request):
	return render(request, 'campus/love.html')

def learn(request):
	return render(request, 'campus/learn.html')

def forgotPassword(request):
	return render(request, 'campus/forgotPassword.html')

#发送邮件
def setEmail(request):
	email = request.POST.get('email', '')
	user = models.User.objects.filter(email=email)
	request.session['userName'] = user[0].userName
	subject = '请重置您的密码'
	text_content = '请重置您的密码'
	html_content = '<p>这是一封<strong>重要的</strong>邮件.</p><a  href="http://192.168.1.104:8000/mycampus/rePassword/'+'">'+'点击这里重置密码</a>'
	msg = EmailMultiAlternatives(subject, text_content, '2384236461@qq.com', [email])
	msg.attach_alternative(html_content, "text/html")
	msg.send()
	return redirect('/mycampus/login/')
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