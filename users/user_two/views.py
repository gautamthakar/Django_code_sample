from django.shortcuts import render
from django.http import HttpResponse
from user_two.models import Users
# Create your views here.

def index(request):
    ind_cont={'message1':'Welcome to Index page', 'message2':'Please browse to /users to get user information'}
    return render(request, 'user_two/index.html', context=ind_cont)

def users(request):
    get_user=Users.objects.order_by('firstname')
    user_dict={'user_info':get_user}
    return render(request,'user_two/users.html', context=user_dict)
