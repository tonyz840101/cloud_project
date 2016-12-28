from django.conf.urls import url
from . import views

app_name = 'another'

urlpatterns = [
	url(r'^$',views.Index,name='indexs'),
	url(r'^upload$',views.Upload,name='upload'),
	url(r'^download$',views.Download,name='download'),
	url(r'^table$',views.Table,name='table'),
]

