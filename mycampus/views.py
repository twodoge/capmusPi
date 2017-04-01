#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
 
def login(request):
    return render(request, 'campus/login.html')

def  register(request):
	return render(request, 'campus/register.html')

def  index(request):
	return render(request, 'campus/index.html')

def  member(request):
	return render(request, 'campus/member.html')
	
def  published(request):
	return render(request, 'campus/published.html')

def love(request):
	return render(request, 'campus/love.html')

def learn(request):
	return render(request, 'campus/learn.html')