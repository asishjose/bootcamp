from django.shortcuts import render
from django.contrib.auth.models import User#since the auth module is not created by us, we have to import it for user creation.

# Create your views here.

def signup(request):
    user=None
    error_message=None
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=User.objects.create_user(username=username,password=password)
        except Exception as e:
            error_message=str(e)
    return render(request,'users/create.html',{'user':user,'error_message':error_message})