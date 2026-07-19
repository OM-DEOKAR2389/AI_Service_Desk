from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from accounts.decorators import role_required
from accounts.models import User
from django.db.models import Q


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


def admin_dashboard(request):
    total_users = User.objects.count()
    total_engineers = User.objects.filter(role='Engineer').count()
    total_admins = User.objects.filter(role='Admin').count()
    total_normal_users = User.objects.filter(role='User').count()

    context = {
        'total_users': total_users,
        'total_engineers': total_engineers,
        'total_admins': total_admins,
        'total_normal_users': total_normal_users,
    }

    return render(request, 'dashboard/admin_dashboard.html', context)



@login_required(login_url='login')
@role_required(['Admin'])
def user_list(request):

    search = request.GET.get('search', '')

    users = User.objects.all().order_by('-id')

    if search:
        users = users.filter(
            Q(username__icontains=search) |
            Q(email__icontains=search) |
            Q(phone__icontains=search)
        )

    return render(request, 'dashboard/user_list.html', {
        'users': users,
        'search': search,
    })