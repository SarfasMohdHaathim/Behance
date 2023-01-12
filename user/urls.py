from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup,name="signup"),
    path('userlogin/', views.userlogin,name="userlogin"),
    path('userlogout/', views.userlogout,name="userlogout"),
    path('profile/', views.profile,name="profile"),
    path('addProfile/', views.addProfile,name="addProfile"),
]