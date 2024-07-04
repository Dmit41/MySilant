from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin

from accounts.forms import AdminRegisterForm, LoginUserForm
from accounts.models import *


class RegisterUser(PermissionRequiredMixin, CreateView):
    permission_required = ('account.add_user',)
    model = User
    form_class = AdminRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('main')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('main')


def logout_view(request):
    logout(request)
    return redirect('main')



