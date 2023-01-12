from django.db import models
from user.models import Profile

# Create your models here.


class Post(models.Model):
    profile=models.ForeignKey(Profile,blank=True,null=True,on_delete=models.SET_NULL)
    title=models.CharField(max_length=100)
    des=models.TextField()
    cover=models.ImageField(upload_to="media",blank=True,null=True)
    img1=models.ImageField(upload_to="media",blank=True,null=True)
    img2=models.ImageField(upload_to="media",blank=True,null=True)
    img3=models.ImageField(upload_to="media",blank=True,null=True)
    like=models.IntegerField(blank=True,null=True,default=0)



    def __str__(self):
        return self.title



class Appreciate(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    liked=models.BooleanField(default=False)
    


class Follow(models.Model):
    following = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, related_name="following")
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, related_name="follower")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.following)

    class Meta:
        unique_together = ("following", "follower")

   


class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    coment_date=models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="messages")
    name = models.CharField(max_length=200, blank=True, null=True)
    is_read = models.BooleanField(default=False)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    class Meta:
        ordering = ['is_read', '-created']



class SavePost(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


