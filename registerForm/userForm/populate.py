import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'userForm.settings')

import django 
django.setup()


from faker import Faker 
from zapform.models import UserID 

def populate(N=5):
    fakergen = Faker()

    for s in range(N):

        usname = fakergen.user_name()
        email_address = fakergen.email()

        UserID.objects.get_or_create(username= usname, email=email_address )
        

if __name__ == '__main__':
    populate(10)
    print("Just done populating!")


