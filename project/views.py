# -*- coding: UTF-8 -*-
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,login,logout
from datetime import datetime
from .models import Measuring_data,User_image
import json, requests,os

# Create your views here.


def Index(request):
	if request.POST.get('register',None):		
		username = request.POST.get('username',None)
		password = request.POST.get('password',None)
		passwd = request.POST.get('passwd',None)
		account_type =  request.POST.get('account_type',None)
		staff = ''
		user = ''
		very = request.POST.get('very',None)
		if username and password and passwd and account_type:
			if account_type == 'staff':
				staff = 'checked'
			else:
				user = 'checked'
			if password == passwd:
				if User.objects.filter(username=username).exists():
					return render(request,'project/register.html',{
                		        	'error': 'Username has already been taken',
						'username':username,
						'staff': staff,
						'user': user,
                			})
				elif account_type=='staff' and very != '123456789':
					return render(request, 'project/register.html', {
						'error': 'Authentication Code Error',
						'username': username,
						'staff': staff,
						'user': user,
					})
				else:
					user = User.objects.create_user(username,username,password)
					group = Group.objects.get(name=account_type)
					user.groups.add(group)
					user.save()
					return render(request,'project/login.html',{
	                                        'message': 'Successful',
											'color': 'black',
	                                })


			else:
				return render(request,'project/register.html',{
					'error': 'Password Inconsistent',
					'username':username,
                                        'staff': staff,
                                        'user': user,

				})
		else:
			return render(request,'project/register.html',{
				'error': 'Complete the Form',
				'username':username,
                                'staff': staff,
                                'user': user,
	
			})
	else:
		username = request.POST.get('username',None)
		password = request.POST.get('password',None)
		if username and password:
			user = authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				return redirect('/index')
			else:
				return render(request,'project/login.html',{
					'message': 'Login Failed',
					'color': 'red',
				})
		if request.user.is_authenticated:
			if str(request.user.groups.all()[0]) == 'staff':
				return render(request,'project/staff_index.html',{
					})
			else :
				data = Measuring_data.objects.filter(email=request.user.username)
				if data.__len__() :
					image_file = 'image/default.jpg'
					if User_image.objects.filter().exists():
						image_file = 'image/%s' % (str(User_image.objects.filter(username=request.user.username)[0].image).split('/')[-1])
					return render(request, 'project/table.html',{
						'table': data,
						'user_test': data[0].email,
						'gender' : data[0].gender,
						'image_file': image_file,
						'is_user' : 1,
					})
				else :
					return render(request, 'project/empty_table.html')

		else:
			return render(request,'project/login.html')
def Register(request):
	return render(request,'project/register.html')


def Logout(request):
	logout(request)
	return redirect('/index')
	
def Edit(request):
	userlist = set()
	for user in Group.objects.get(name='user').user_set.all():
		userlist.add(user.username)
	if request.user.is_authenticated and str(request.user.groups.all()[0]) == 'staff':
		return render(request,'project/staff_fill_in.html',{
			'userlist' : sorted(userlist),
		})
	else :
		return render(request,'project/login.html')
		
def Submit(request):
	if request.user.is_authenticated and str(request.user.groups.all()[0]) == 'staff':
		datetime = request.POST.get('datetime','')
		email = request.POST.get('email','')
		grade = request.POST.get('grade','')
		age = request.POST.get('age','1')
		gender = request.POST.get('gender','')
		height = request.POST.get('height',0)
		weight = request.POST.get('weight',0)
		avg_ex_hour = request.POST.get('avg_ex_hour',0)
		stomach = request.POST.get('stomach','')
		avg_sleep_hour = request.POST.get('avg_sleep_hour',0)
		mood = request.POST.get('mood','')

		txt = request.FILES.get('txt', '')

		
		measure = Measuring_data.objects.create(datetime=datetime)
		
		measure.email = email
		measure.grade = grade
		measure.age = age
		measure.gender = gender
		measure.height = height
		measure.weight = weight
		measure.avg_ex_hour = avg_ex_hour
		measure.stomach = stomach
		measure.avg_sleep_hour = avg_sleep_hour
		measure.mood = mood
		measure.txt = txt
		txt.name = '%s_%s.txt'%(email,datetime)

		measure.save()

		return redirect('/index')
		
	else :
		return redirect('/index')


def Staff_right(request):
	user = request.GET.get('user',None)
	if user is None :
		return render(request, 'project/empty_table.html')
	gender = '女'
	if Measuring_data.objects.filter(email=user).__len__() == 0:
		return render(request, 'project/empty_table.html')
	else :
		if Measuring_data.objects.filter(email=user) and Measuring_data.objects.filter(email=user)[0].gender == 'male':
			gender='男'
		image_file = 'image/default.jpg'
		if gender=='女':
			image_file = 'image/default_female.jpg'

		if User_image.objects.filter(username=user).exists():
			image_file = 'image/%s'%(str(User_image.objects.filter(username=user)[0].image).split('/')[-1])

		return render(request, 'project/table.html',{
			'table': Measuring_data.objects.filter(email=user),
			'user_test': user,
			'gender' : gender,
			'image_file': image_file,
		})

def Staff_left(request):
	userlist = set()
	for user in Group.objects.get(name='user').user_set.all():
		userlist.add(user.username)
	return render(request, 'project/staff_left.html',{'userlist':sorted(userlist)})

def Table(request):
	return HttpResponse("hello Table")

def Download(request):
    filename =  Measuring_data.objects.filter(txt=request.GET['file'])[0]
    response = HttpResponse(filename.txt, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=%s' % (str(request.GET['file']).split('/')[-1])
    return response

def Edit_image(request):
	image_file = request.GET.get('image_file','')
	username = request.GET.get('username','')
	return render(request,'project/upload_image.html',{
		'username':username,
		'image_file':image_file,})

def Upload_image(request):
	image = request.FILES.get('image', None)
	username = request.POST.get('username', None)
	user_image = User_image.objects.filter(username=username)
	if user_image.__len__():
		user_image[0].image.storage.delete(user_image[0].image.path)
		user_image[0].delete()
	image.name = '%s.%s'%(username,image.name.split('.')[-1])
	user_image = User_image.objects.create(username=username,image=image)
	user_image.save()
	return redirect('/staff_right?user=%s'%(username))

def Api(request):
	username = request.GET.get('username','')
	data = Measuring_data()


	if Measuring_data.objects.filter(email=username).__len__():
		data = Measuring_data.objects.filter(email=username)[0]
	datas = {
		'grade': data.grade,
		'age' : data.age,
		'gender': data.gender,
		'height': data.height,
		'weight': data.weight,
	}
	datas = json.dumps(datas)
	return HttpResponse(datas)
