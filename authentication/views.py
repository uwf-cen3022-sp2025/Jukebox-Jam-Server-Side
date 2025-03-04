# these packages will help with user authentication (logging in)
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from .forms import RegisterForm
from django.core.exceptions import ValidationError
import re

#Django packages for email
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
        # this package just fetches the site
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator

User = get_user_model()

# define views with the "def" keyword
def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # make sure username is longer than 5 chars
        if len(username) < 5:
            messages.error(request, "Username must be at least 5 characters long")
            return redirect('register')

        # make sure email is valid
        accepted_email_domains = ["gmail.com", "outlook.com", "yahoo.com", "hotmail.com", "icloud.com", "cox.net"]
        domain = email.split('@')[-1]
        # check to see if domain is NOT IN array of allowed domains
        if domain not in accepted_email_domains:
            messages.error(request, f"Requested email domain not accepted, use: {', '.join(accepted_email_domains)}")
            return redirect('register')

        # password verification
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if password != confirm_password:
            raise ValidationError("Passwords do not match")
        if not re.search(r"\d", password):
            raise ValidationError("Password must contain at least a number")
        if not re.search(r"[A-Z]", password):
            raise ValidationError("Password must contain at least one uppercase letter")

        # check if email and username already exist
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists!")

        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already registered!")

        # Generate a temporary user that will be sent to the email confirmation view
        temp_user = User(username=username, email=email)
        temp_user.set_password(password)
        temp_user.is_active = False  # must confirm email

        # send the email through view call
        send_email_confirmation(request, temp_user)

        messages.success(request, "Check your email for a confirmation link")
        return redirect('login')
    else:
        return render(request, "register.html")


def login_view(request):
        if request.method == 'POST':
                # just like register, handle it same way
                return HttpResponse("Login logic here")
        return render(request, 'login.html')

def logout_view(request):
        logout(request)
        return redirect('/login/')


# SEND CONFIRM EMAIL

def send_email_confirmation(request, user):
        # make a token
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        domain = get_current_site(request).domain
        # SEND LINK
        link = reverse('confirm_email', kwargs={'uidb64': uid, 'token': token})
        # create confirm email (http://{domain}{link})
        confirm_email_url = f'http://{domain}{link}'
# this is email format - create subject than a body
        email_subject = 'Confirm your Email'
        email_body = render_to_string('authentication/email_confirmation.html', {'confirm_email_url': confirm_email_url})

        send_mail(email_subject, email_body, 'no-reply@jukebox-jam.com', [user.email])

# a new view to see if email is confirmed
def email_confirm(request, uidb64, token):
        # use trycatch block
        try:
                uid = force_str(urlsafe_base64_decode(uidb64))
                user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
                user = None

        if user is not None and default_token_generator.check_token(user, token):
                user.is_active = True
                user.save()
                #return to the login after confirmation
                return redirect('login')
        else:
                return HttpResponse('Invalid confirm link', status=400)