from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from .models import LoginModel

class LoginList(ListView):
    model = LoginModel
    fields = ['username', 'password']  # Adjust the fields based on your model attributes
    template_name = 'loginmodel_form.html'  # Specify the template name

    # Optionally, you can override the success URL or other attributes
    success_url = '/login-success/'  # Change this to the URL you want to redirect to upon successful form submission
