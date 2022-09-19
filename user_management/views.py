
from django.shortcuts import render

from .forms import LoginModelForm

from .serializers import UserSerializer

from rest_framework import viewsets

from django.views.generic import FormView, RedirectView

from django.contrib.auth import authenticate, login

# Create your views here.

class Login_view(FormView):
    template_name = 'user_management/login.html'
    form_class = LoginModelForm
    success_url = '/'


    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(self.request,user)
        return super().form_valid(form)


    





