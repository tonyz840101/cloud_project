from django.contrib import admin
from .models import Test,Client_secret,Measuring_data,User_image
# Register your models here.

admin.site.register(Test)
admin.site.register(Client_secret)
admin.site.register(Measuring_data)
admin.site.register(User_image)