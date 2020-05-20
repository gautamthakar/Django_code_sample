from user_two import views
from django.urls import *

urlpatterns=[
    path('',views.index,name='index'),
    path('users/',views.users,name='users'),
]
