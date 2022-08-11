from . import views
from django.urls import path

app_name = 'accounts' 
urlpatterns = [        
    path('',views.index, name='index'),
<<<<<<< HEAD
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('resetpassword/', views.reset, name='resetpassword'),
    path('forgotpassword/', views.forgot, name='forgetpassword'),       
=======
    path('/register', views.register, name='register'),
    path('/login', views.login_user, name='login') 
    path('register', views.register, name='register'),       
>>>>>>> 00aa4bb62df58b79ee97b025f41693187325bbb1
    path('contact', views.contact, name='contact'),
] 