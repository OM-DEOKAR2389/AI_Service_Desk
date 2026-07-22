from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import role_required
from .forms import TicketForm
from django.db.models import Q
from .models import Ticket
from django.contrib import messages
from accounts.models import User






@login_required(login_url='login')
@role_required(['User'])
def raise_ticket(request):

    if request.method == "POST":

        form = TicketForm(request.POST)

        if form.is_valid():

            ticket = form.save(commit=False)

            ticket.user = request.user

            ticket.save()

            return redirect('my_tickets')

    else:

        form = TicketForm()

    context = {
        'form': form
    }

    return render(request, 'tickets/raise_ticket.html', context)



@login_required(login_url='login')
@role_required(['User'])
def my_tickets(request):

    tickets = Ticket.objects.filter(
        user=request.user
    ).order_by('-created_at')

    context = {
        'tickets': tickets
    }

    return render(request, 'tickets/my_tickets.html', context)



@login_required(login_url='login')
@role_required(['User'])
def ticket_detail(request, id):

    ticket = get_object_or_404(
        Ticket,
        id=id,
        user=request.user
    )

    context = {
        'ticket': ticket
    }

    return render(
        request,
        'tickets/ticket_detail.html',
        context
    )
    


@login_required(login_url='login')
@role_required(['Admin'])
def all_tickets(request):

    search = request.GET.get('search')

    tickets = Ticket.objects.all().order_by('-created_at')

    if search:

        tickets = tickets.filter(

            Q(title__icontains=search) |

            Q(user__username__icontains=search) |

            Q(category__icontains=search)

        )

    context = {

        'tickets': tickets,

        'search': search

    }

    return render(
        request,
        'tickets/all_tickets.html',
        context
    )
    


@login_required(login_url='login')
@role_required(['Admin'])
def admin_ticket_detail(request, id):

    ticket = get_object_or_404(Ticket, id=id)

    engineers = User.objects.filter(role="Engineer")

    if request.method == "POST":

        engineer_id = request.POST.get("engineer")

        if engineer_id:

            ticket.assigned_engineer = User.objects.get(id=engineer_id)

            ticket.save()

            messages.success(
                request,
                "Engineer assigned successfully."
            )

            return redirect("all_tickets")

    context = {

        "ticket": ticket,

        "engineers": engineers

    }

    return render(
        request,
        "tickets/admin_ticket_detail.html",
        context
    )
    
    
@login_required(login_url='login')
@role_required(['Engineer'])
def assigned_tickets(request):

    tickets = Ticket.objects.filter(
        assigned_engineer=request.user
    ).order_by('-created_at')

    context = {
        "tickets": tickets
    }

    return render(
        request,
        "tickets/assigned_tickets.html",
        context
    )
    
    
@login_required(login_url='login')
@role_required(['Engineer'])
def engineer_ticket_detail(request, id):

    ticket = get_object_or_404(
        Ticket,
        id=id,
        assigned_engineer=request.user
    )

    if request.method == "POST":

        ticket.status = request.POST.get("status")
        ticket.resolution = request.POST.get("resolution")

        ticket.save()

        return redirect("assigned_tickets")

    context = {
        "ticket": ticket
    }

    return render(
        request,
        "tickets/engineer_ticket_detail.html",
        context
    )