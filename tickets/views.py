from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import role_required
from .forms import TicketForm


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

from .models import Ticket


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

from django.shortcuts import get_object_or_404


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