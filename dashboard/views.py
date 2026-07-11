from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from accounts.decorators import role_required


def admin_dashboard(request):
    return HttpResponse("<h1>Admin Dashboard</h1>")


def user_dashboard(request):
    return HttpResponse("<h1>User Dashboard</h1>")


def engineer_dashboard(request):
    return HttpResponse("<h1>Engineer Dashboard</h1>")






@login_required(login_url='login')
@role_required(['Admin'])
def admin_dashboard(request):
    return render(request, 'dashboard/admin_dashboard.html')


@login_required(login_url='login')
@role_required(['User'])
def user_dashboard(request):
    return render(request, 'dashboard/user_dashboard.html')


@login_required(login_url='login')
@role_required(['Engineer'])
def engineer_dashboard(request):
    return render(request, 'dashboard/engineer_dashboard.html')