import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','users.settings')

import django.conf
django.setup()
##Facker Script

from user_two.models import Users
from faker import Faker

fakegen=Faker()

def populate(N=5):
    for entry in range(N):

        fake_name= fakegen.name()
        name=fake_name.split(" ")
        fake_fn= name[0]
        fake_ln= name[1]
        fake_email=fakegen.email()

        add_user=Users.objects.get_or_create(firstname=fake_fn, lastname=fake_ln, email=fake_email)[0]

if __name__=='__main__':
    print("Populating Script!")
    populate(25)
    print("Populating Complete :) ")
