from django.urls import path
from . import views
# from django.conf.urls import include


urlpatterns = [
	path('singup', views.singup, name='singup'),
	path('singup_done', views.singup_done, name='singup_done'),
	path('error', views.error, name='error'),
	path('', views.index, name='index'),
	path('singin', views.singin, name='singin'),
	path('controlPanel', views.control_panel, name='controlPanel')
]
