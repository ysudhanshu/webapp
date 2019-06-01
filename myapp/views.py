from django.shortcuts import render
#Adding to git repository
# Create your views here.

def index(request):
    return render(request, template_name='myapp/index.html')


def myapp_home(request):
    return render(request, template_name='myapp/myapp_home.html')

def user_login(request):
    return render(request, template_name='myapp/user_login.html')