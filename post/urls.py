
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.home,name="home"),
    path('postDesk/<str:pk>', views.postDesk,name="postDesk"),
    path('about/', views.about,name="about"),
    path('delete/<str:pk>', views.DeletePost,name="DeletePost"),
    path('createpost/',views.createPost,name="createPost"),
    path('gallary/',views.gallary,name="gallary"),
    path('inbox/',views.inbox,name="inbox"),
    path('search/',views.search,name="search"),
    path('saved/',views.saved,name="saved"),
    path('header/',views.header,name="header"),
    path('replymsg/',views.replymsg,name="replymsg"),
    path('message/<str:pk>',views.message,name="message"),
    path('follow/<str:data>',views.follow,name="follow"),
    path('createmessage/<str:pk>', views.createmessage,name="createmessage"),
    path('updatepost/<str:pk>',views.UpdatePost,name="UpdatePost"),
    path('appreciate/<str:pk>',views.appreciate,name="appreciate"),
    path('savepost/<str:pk>',views.savepost,name="savepost"),
  
    
]
