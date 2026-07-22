from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from accounts.decorators import role_required
from accounts.models import User
from django.db.models import Q
from tickets.models import Ticket


def user_dashboard(request):
    return HttpResponse("<h1>User Dashboard</h1>")


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
    
@login_required(login_url='login')
@role_required(['Engineer'])
def engineer_dashboard(request):

    total = Ticket.objects.filter(
        assigned_engineer=request.user
    ).count()

    open_ticket = Ticket.objects.filter(
        assigned_engineer=request.user,
        status='Open'
    ).count()

    progress = Ticket.objects.filter(
        assigned_engineer=request.user,
        status='In Progress'
    ).count()

    resolved = Ticket.objects.filter(
        assigned_engineer=request.user,
        status='Resolved'
    ).count()

    recent_tickets = Ticket.objects.filter(
        assigned_engineer=request.user
    ).order_by('-created_at')[:5]

    context = {
        'total': total,
        'open_ticket': open_ticket,
        'progress': progress,
        'resolved': resolved,
        'recent_tickets': recent_tickets,
    }

    return render(
        request,
        'dashboard/engineer_dashboard.html',
        context
    )
    
@login_required(login_url='login')
@role_required(['Engineer'])
def engineer_dashboard(request):

    total = Ticket.objects.filter(
        assigned_engineer=request.user
    ).count()

    open_ticket = Ticket.objects.filter(
        assigned_engineer=request.user,
        status='Open'
    ).count()

    progress = Ticket.objects.filter(
        assigned_engineer=request.user,
        status='In Progress'
    ).count()

    resolved = Ticket.objects.filter(
        assigned_engineer=request.user,
        status='Resolved'
    ).count()

    recent_tickets = Ticket.objects.filter(
        assigned_engineer=request.user
    ).order_by('-created_at')[:5]

    context = {

        'total': total,
        'open_ticket': open_ticket,
        'progress': progress,
        'resolved': resolved,
        'recent_tickets': recent_tickets,

    }

    return render(request, 'dashboard/engineer_dashboard.html', context)

@login_required(login_url='login')
@role_required(['Admin'])
def admin_dashboard(request):

    total_users = User.objects.filter(role='User').count()

    total_engineers = User.objects.filter(role='Engineer').count()

    total_tickets = Ticket.objects.count()

    open_ticket = Ticket.objects.filter(status='Open').count()

    progress = Ticket.objects.filter(status='In Progress').count()

    resolved = Ticket.objects.filter(status='Resolved').count()

    recent_tickets = Ticket.objects.select_related(
        'user',
        'assigned_engineer'
    ).order_by('-created_at')[:5]
    
    recent_users = User.objects.order_by('-date_joined')[:5]

    context = {

        'total_users': total_users,
        'total_engineers': total_engineers,
        'total_tickets': total_tickets,
        'open_ticket': open_ticket,
        'progress': progress,
        'resolved': resolved,
        'recent_tickets': recent_tickets,
        'recent_users': recent_users,

    }

    return render(request, 'dashboard/admin_dashboard.html', context)

@login_required(login_url='login')
@role_required(['User'])
def user_dashboard(request):

    total = Ticket.objects.filter(user=request.user).count()

    open_ticket = Ticket.objects.filter(
        user=request.user,
        status='Open'
    ).count()

    progress = Ticket.objects.filter(
        user=request.user,
        status='In Progress'
    ).count()

    resolved = Ticket.objects.filter(
        user=request.user,
        status='Resolved'
    ).count()

    recent_tickets = Ticket.objects.filter(
        user=request.user
    ).order_by('-created_at')[:5]

    context = {
        'total': total,
        'open_ticket': open_ticket,
        'progress': progress,
        'resolved': resolved,
        'recent_tickets': recent_tickets,
    }

    return render(request, 'dashboard/user_dashboard.html', context)