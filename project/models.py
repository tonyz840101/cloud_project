from __future__ import unicode_literals

from django.db import models

# Create your models here.

def user_directory_path(instance, filename):
    return './project/user_{0}/{1}'.format(instance.email,filename)
def user_directory_iamgepath(instance, filename):
    return './project/static/image/{0}'.format(filename)

class Test(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name
class Client_secret(models.Model):
	name = models.CharField(max_length=200)
	client_secret = models.CharField(max_length=200)
	client_id = models.CharField(max_length=200)
	refresh_token = models.CharField(max_length=200)
	def __str__(self):
        	return self.name
class Measuring_data(models.Model):
	datetime = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	grade = models.CharField(max_length=200)
	age = models.IntegerField(default=0)
	gender = models.CharField(max_length=200)
	height = models.FloatField(default=0)
	weight = models.FloatField(default=0)
	avg_ex_hour = models.FloatField(default=0)
	stomach = models.CharField(max_length=200)
	avg_sleep_hour = models.FloatField(default=0)
	mood = models.CharField(max_length=200)
	txt = models.FileField(upload_to=user_directory_path, default='')
	def __str__(self):
        	return self.email


class User_image(models.Model):
	username = models.CharField(max_length=100)
	image = models.FileField(upload_to=user_directory_iamgepath)

	def __str__(self):
		return self.username
