from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User 
from django.conf import settings
from django.core.mail import send_mail
from .models import *
from post.models import *
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
            try:
                subject = 'welcome to BEHANCE'
                message = f'Hi {user.username}, thank you for registering in BEHANCE.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email]
                send_mail( subject, message, email_from, recipient_list )
                return redirect('home')
            except:
                print("email failed")
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
    follow=Follow.objects.filter(follower=profile)
    print(follow)
    context={'profile':profile,'name':name,'follow':follow}
    return render(request, 'profile.html',context)   



def addProfile(request):
    profile=request.user.profile
    forms=ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            print(form,"0000000000")

            form.save()
            return redirect('profile')

    context={'forms':forms}
    return render(request, 'addprofile.html',context)   


def unfollow(request,pk):
    print(pk,'00000000000000000000')
    profile=Profile.objects.get(user=request.user)
    print(profile.id)
    d=Profile.objects.get(id=pk)
    follow=Follow.objects.get(following=d,follower=profile).delete()
    return redirect('profile')



# def follow(request, data):
#     print(request.user.first_name,'00000000000000000000')
#     profile=Profile.objects.get(username=request.user.username)
#     print(profile)
#     follower = Profile.objects.get(id=data)
#     try:
#         follow = Follow.objects.create(following=profile, follower=follower)
#     except:
#         follow = Follow.objects.filter(following=profile, follower=follower)
#         follow.delete()
#     return redirect('home')