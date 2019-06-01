from django.urls import path
from myapp import views

app_name = 'myapp'

urlpatterns = [
    path('', views.myapp_home, name='myapp_home'),
    ]
