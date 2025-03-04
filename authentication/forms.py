from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import CustomerUser

import re

# allow these domains
ALLOWED_DOMAINS = ["gmail.com", "outlook.com", "icloud.com", "yahoo.com", "hotmail.com", "cox.net"]


def validate_email_domain(email):
    # create domain entity that splits the email after '@', then throw error if not allowed
    domain = email.split('@')[-1]

    if domain not in ALLOWED_DOMAINS:
        raise ValidationError("Email domain not accepted currently, please enter email with valid domain: " + ", ".join(ALLOWED_DOMAINS))
    

def validate_password_length(password):
    # if password is less than 8 characters, throw error
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long")
    # use re.search to look through the password for requirements
    if not re.search(r"\d", password):
        raise ValidationError("Password must contain at least 1 number.")
    if not re.search(r"[A-Z]", password):
        raise ValidationError("Password must have at least one uppercase letter.")

# this class is for the register.html form
class RegisterForm(UserCreationForm):
    email = forms.EmailField(validators=[validate_email_domain])

    password1 = forms.CharField(
        label = "Password",
        widget=forms.PasswordInput,
        validators=[validate_password_length],
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput,
        validators=[validate_password_length],
    )

    class Meta:
        model = CustomerUser
        fields = ["username", "email", "password1", "password2"]