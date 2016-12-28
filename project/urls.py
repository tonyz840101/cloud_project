from django.conf.urls import url
from . import views

app_name = 'project'
urlpatterns = [
	url(r'^$',views.Index,name='indexs'),
	url(r'^index$',views.Index,name='index'),
	url(r'^register$',views.Register,name='register'),
	url(r'^logout$',views.Logout,name='logout'),
	url(r'^edit$',views.Edit,name='edit'),
	url(r'^submit$',views.Submit,name='submit'),
	url(r'^table',views.Table,name='table'),
	url(r'^staff_left',views.Staff_left,name='staff_left'),
	url(r'^staff_right',views.Staff_right,name='staff_right'),
	url(r'^download',views.Download,name='download'),
	url(r'^upload_image',views.Upload_image,name='upload_image'),
	url(r'^edit_image',views.Edit_image,name='edit_image'),
	url(r'^api',views.Api,name='api'),

]

