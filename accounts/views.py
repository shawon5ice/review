from django.shortcuts import render,redirect 
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/login.html',{'error':'username or password is incorrect'})
    else:
        return render(request,'accounts/login.html')



def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')



def signup(request):
    if request.method == 'POST':
        #user ha info and want to sign up
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'accounts/signup.html',{'error':'Username has already been taken'})
            except User.DoesNotExist:
                user =User.objects.create_user(username=request.POST['username'],password = request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
                return render(request,'accounts/signup.html',{'perror':'Password does not matched'})
    else:
        return render(request,'accounts/signup.html')


    