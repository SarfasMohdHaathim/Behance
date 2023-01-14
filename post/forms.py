from django import forms
from django.forms import ModelForm
from .models import *


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','des','cover','img1','img2','img3']
        labels = {
            'title': 'Title of Post',
            'des': 'Description',
            'cover': 'Cover Image ',
            'img1': 'Image 1',
            'img2': 'Image 2',
            'img3': 'Image 3'
        }





class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'body']