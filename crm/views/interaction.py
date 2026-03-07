from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from crm.models import Interaction, Customer
from crm.forms import InteractionForm


def add_interaction(request, id: int):
    customer = get_object_or_404(Customer, pk=id)

    form = InteractionForm({
        'customer': customer
    })

    if request.method == 'GET':
        return render(request, 'form.html', context={
            'form': form,
            'method': 'POST',
            'action': f'/customer/{id}/interaction/add/'
        })

    form = InteractionForm(request.POST)

    if not form.is_valid():
        for _, error in form.errors.items():
            messages.add_message(request, messages.ERROR, error)

        return render(request, 'form.html', context={
            'form': form,
            'method': 'POST',
            'action': f'/customer/{id}/interaction/add/',
            'messages': messages.get_messages(request),
        })        

    form.save()
    return redirect('/customer/')
