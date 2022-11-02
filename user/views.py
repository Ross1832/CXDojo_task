from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import UploadFileForm, UserForm, UpdateUserForm
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import User
import csv


@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponseRedirect(reverse_lazy('user:list'))
    else:
        form = UploadFileForm()
    return render(request, 'user/upload.html', {'form': form})


class ListUserView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user/list.html'


class CreateUserView(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'user/user_form.html'
    success_url = reverse_lazy('user:list')
    form_class = UserForm


class UpdateUserView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'user/user_form.html'
    success_url = reverse_lazy('user:list')
    form_class = UpdateUserForm


class DetailUserForm(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user/detail.html'
    context_object_name = 'user'


class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'user/delete.html'
    success_url = reverse_lazy('user:list')


def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Users ' + str(datetime.now()) + '.csv'
    writer = csv.writer(response)
    writer.writerow(['Username', 'First_name', 'Last_name', 'Date_joined'])
    users = User.objects.all()

    for user in users:
        writer.writerow([user.username, user.first_name, user.last_name, user.date_joined])

    return response
