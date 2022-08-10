from . import views
from django.urls import path

app_name = 'accounts' 
urlpatterns = [        
    path('',views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('resetpassword/', views.reset, name='resetpassword'),
    path('forgotpassword/', views.forgot, name='forgetpassword'),       
    path('contact', views.contact, name='contact'),
] 