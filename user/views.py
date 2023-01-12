from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User 
from django.conf import settings
from django.core.mail import send_mail
from .models import *
from .forms import *


# Create your views here.

def signup(request):
    form=CustomUserCreationForm()
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            subject = 'welcome to BEHANCE'
            message = f'Hi {user.username}, thank you for registering in BEHANCE.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            send_mail( subject, message, email_from, recipient_list )
            return redirect('home')
        else:
            print("Error")
            return redirect('signup')
    context={'form':form}

    return render(request,'signup.html',context)


def userlogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=User.objects.get(username=username)
        except:
            print('user is not found')
    
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            print('invalid Credential')

    return render(request,'login.html')


def userlogout(request):
    logout(request)
    return redirect('home')







def profile(request):
    profile=Profile.objects.get(user=request.user)
    print(profile,'000000000000000')
    name=profile.name.capitalize()
    context={'profile':profile,'name':name}
    return render(request, 'profile.html',context)   



def addProfile(request):
    profile=request.user.profile
    forms=ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context={'forms':forms}
    return render(request, 'addprofile.html',context)   


