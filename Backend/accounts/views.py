from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Lib
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from . tokens import generate_token


# Create your views here.


# Landing page view
def index(request):
    animation_objects = Lib.objects.all()
    animation_types = []
    for animation in animation_objects:
        if animation.anima_type not in animation_types:
            animation_types.append(animation.anima_type) 
    paginator = Paginator(animation_types,8)
    page = request.GET.get('page') 
    animation_types = paginator.get_page(page)  
    context = {
        'animation_types': animation_types,
        'animation_objects': animation_objects        
    } 
    return render(request, 'accounts/index.html', context) 


#Registration page
def register(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email = email):
            messages.error(request, "Email already register")
            return redirect('register')

        # if User.objects.filter(email = email):
        #     messages.error(return redirect('login')quest, "Email already exist")
        
        myuser = User.objects.create_user(username, email, password)
        myuser.is_active = False
        myuser.save()

        messages.success(request, "Your Account has been successfully created. We have sent you a confirmation email")

        #Email Address Confirmation Email

        current_site = get_current_site(request)
        email_subject = "Confirm your email @ accounts - Django Login!!"
        message2 = render_to_string("email_confirmation.html"),{
            'name': username,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        }
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()

        return redirect('login')

    return render(request, "accounts/registration.html")

#Login page
def login(request):

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email = email, password = password)

        if user is not None:
            login(request, user)
            return redirect(request, "accounts/homepage.html")

        else:
            messages.error(request, "Incorrect email or password.")
            return redirect(request, "accounts/login.html")

    return render(request, "accounts/login.html")

#Logout page
def logout(request):
    logout(request, user)
    messages.success(request, "Logged out Successfully")
    return render(request, "accounts/index.html")

#Reset password page
def reset(request):
    return render(request, "accounts/resetpassword.html")

#Forgot password page
def forgot(request):
    return render(request, "accounts/forgotpassword.html")

#Login page
# def login(request):
#     return render(request, "accounts/login.html")


# Profile page view
@login_required
def profilepage(request):
    return render(request, 'accounts/profile.html')

#ContactUs Page View

def contact(request):
    return render(request, 'accounts/contact.html')