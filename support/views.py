from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import SupportTicket, SupportResponse
from .forms import SupportTicketForm, SupportResponseForm



def support(request):
    return render(request,'support.html')



@login_required
def ticket_list(request):
    tickets = SupportTicket.objects.filter(user=request.user)
    return render(request, 'ticket_list.html', {'tickets': tickets})


@login_required
def ticket_detail(request, pk):
    ticket = get_object_or_404(SupportTicket, pk=pk, user=request.user)
    responses = ticket.responses.all()
    if request.method == "POST":
        form = SupportResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.ticket = ticket
            response.responder = request.user
            response.save()
            messages.success(request, "Your response has been added.")
            return redirect('support:ticket_detail', pk=pk)
    else:
        form = SupportResponseForm()
    return render(request, 'ticket_detail.html', {'ticket': ticket, 'responses': responses, 'form': form})




@login_required
def create_ticket(request):
    if request.method == "POST":
        form = SupportTicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            user = ticket.save()
            messages.success(request, "Your support ticket has been submitted successfully.")
            return redirect('support:ticket_list')  # app_name + view_name
    else:
        form = SupportTicketForm()
    return render(request, 'ticket_form.html', {'form': form})
