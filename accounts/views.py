from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


class AccountLoginView(LoginView):
    template_name = 'accounts/login.html'


class AccountLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'accounts/logout.html'


@login_required
def account_view(request):
    return render(request, 'accounts/profile.html')
