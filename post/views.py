from django.shortcuts import render,redirect
from .models import *
from .forms import *
from user.models import *
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages


def home(request):
    context={}
    post=Post.objects.all()
    print(post)
    i=0

    context['post']=post
    context['i']=i
    print(context)
    for x in post:
        like = Appreciate.objects.filter( post=x).count()
        x.like=like
        x.save()
        print(x.like)
    profile = Profile.objects.get(user=request.user)
    context['profile']=profile
    return render(request, 'index.html',context)




def createPost(request):
    form= PostForm()

    profile = request.user.profile
    if request.method == 'POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.profile=profile
            post.save()
            return redirect('home')
            
    context={'form':form}
    return render(request,'createpost.html',context)


def UpdatePost(request,pk):
    post=Post.objects.get(id=pk)
    form= PostForm(instance=post)
    if request.method == 'POST':
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post=form.save()
            return redirect('home')

    context={'form':form}
    return render(request,'createpost.html',context)
    
def DeletePost(request,pk):
    post=Post.objects.get(id=pk)
    post.delete()
    return redirect('home')



def about(request):
    return render(request, 'about.html')   




def gallary(request):
    post=Post.objects.filter(profile=request.user.profile)
    print(post)
    context={'post':post}
    return render(request, 'galleries.html',context)  



def inbox(request):
    print(request.user)
    profile=Profile.objects.get(user=request.user)
    msg=Message.objects.filter(recipient=profile)
    print(msg)
    context={'msg':msg}
    return render(request, 'inbox.html',context)   


def message(request,pk):
    profile=Profile.objects.get(user=request.user)
    msg=Message.objects.filter(id=pk)
    print(msg)
    context={'msg':msg}
    return render(request, 'message.html',context)   


def replymsg(request):
    if request.method == 'POST':
        msgreply=request.POST['msgreply']
        sender=request.POST['sender']
        print(sender,msgreply,'000000000000000')
        # sender_profile=Profile.objects.get(username=sender)
        profile=Profile.objects.get(user=request.user)
       
        Message.objects.create(sender=profile,recipient=sender,name=profile.name,body=msgreply)
        

    return render(request, 'message.html')   
    



def appreciate(request, pk):
    print(request.user)
    profile=Profile.objects.get(user=request.user)
    post = Post.objects.get(id=pk)
    print(profile,post)
    try:
        appreciate = Appreciate.objects.get(profile=profile, post=post)
        if appreciate.liked == False:
            appreciate.liked = True
            # post.like+=1
            # post.save()
            appreciate.save()
        else:
            appreciate.liked = False
            # post.like-=1
            # post.save()
            appreciate.save()
    except:
        Appreciate.objects.create(profile=profile, post=post,liked=True)
    
    return redirect('postDesk', pk=post.id)




def follow(request, data):
    print(request.user.first_name,'00000000000000000000')
    profile=Profile.objects.get(username=request.user.username)
    print(profile)
    follower = Profile.objects.get(id=data)
    try:
        follow = Follow.objects.create(following=profile, follower=follower)
    except:
        follow = Follow.objects.filter(following=profile, follower=follower)
        follow.delete()
    return redirect('home')

# def unfollow(request, pk):
#     profile = request.user.profile
#     follower = Profile.objects.get(id=pk)
    
#     return redirect(request.META.get('HTTP_REFERER'))







# @login_required(login_url="login")
# def work_single(request, pk):
#     work = Work.objects.get(id=pk)
#     profile = request.user.profile
#     form =Commentform()
#     if request.method == 'POST':
#         form = Commentform(request.POST)
#         comment = form.save(commit=False)
#         comment.work = work
#         comment.profile = request.user.profile
#         comment.save()
#         return redirect('work_single', pk=work.id)

    
#     appreciate = Appreciate.objects.filter(profile=profile, work=work)
#     if appreciate:
#         like = True
#     else:
#         like = False

#     follow = Follow.objects.filter(following=profile, follower=work.profile.id)
#     if follow:
#         followed = True
#     else:
#         followed = False

#     context = {'work':work, 'form':form,'like': like, 'followed': followed}
#     return render(request, 'work/work_single.html', context)


def postDesk(request,pk):
    if request.user.is_authenticated:
        post=Post.objects.get(id=pk)
        title=post.title.capitalize()
        profile=Profile.objects.get(username=request.user.username)
        name=profile.name.capitalize()



    if request.method == 'POST':
        comment=request.POST['comment']
        comment=Comment.objects.create(profile=profile,post=post
        ,text=comment)
    comment=Comment.objects.filter(post=post)
    context={'posts':post,'title':title,'comment':comment,'name':name,'profile':profile}
    try:
        appreciate=Appreciate.objects.get(profile=request.user.profile,post=pk)
        if appreciate.liked == True:
            context['appreciate']=appreciate
    except:
        pass
    return render(request, 'postdesc.html',context)





def createmessage(request, pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()
    try:
        sender = request.user.profile
    except:
        sender = None
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit = False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name =sender.name
                
            message.save()
            return redirect('home')
    context = {'recipient':recipient, 'form':form}
    return render(request, 'message-form.html', context) 


def search(request):
    profile=Profile.objects.all()
    if request.method == 'POST':
        q=request.POST['q']
    if q:
        print(q)
        ser_post = Post.objects.filter(title__icontains=q)
        # Q(title__name__icontains=q) |
        # Q(profile__icontains=q) |
        # Q(des__icontains=q)
    # )

    return render(request,'index.html',{'ser_post':ser_post})


def savepost(request,pk):
    post=Post.objects.get(id=pk)
    profile = Profile.objects.get(user=request.user)



    try:
        savepost=SavePost.objects.get(profile=profile,post=post)
        savepost.delete()
    except:
        savepost=SavePost.objects.create(profile=profile,post=post)
    return redirect('postDesk',pk)


def saved(request):
    profile = Profile.objects.get(user=request.user)
    save_post=SavePost.objects.filter(profile=profile)
    context={'save_post':save_post}
    return render(request,'savedpost.html',context)



def header(request):
    profile = Profile.objects.get(user=request.user)

    return render(request,'header.html',{'profile':profile})