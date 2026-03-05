from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from customer.models import Customer, Interaction
from customer.forms import CustomerForm


def detail_customer(request, id: int):
    customer = get_object_or_404(Customer, pk=id)
    interactions = Interaction.objects.filter(customer=customer)

    return render(request, 'customer/customer-detail.html', context={
        'customer': customer,
        'interactions': interactions
    })


def list_customers(request):
    customers = Customer.objects.all()

    return render(request, 'customer/customer-list.html', context={
        'customers': customers
    })


def add_customer(request):
    if request.method == 'GET':
        return render(request, 'customer/customer-form.html', context={
            'action': '/add/',
            'form': CustomerForm()
        })

    form = CustomerForm(request.POST)
    
    if not form.is_valid():
        for _, error in form.errors.items():
            messages.add_message(request, messages.ERROR, error)

        return render(request, 'customer/customer-form.html', context={
            'action': '/add/',
            'form': CustomerForm(),
            'messages': messages.get_messages(request),
        })

    form.save()

    return redirect('/customer')


def delete_customer(request, id: int):
    customer = get_object_or_404(Customer, pk=id)
    customer.delete()

    return redirect('/customer/')


def update_customer(request, id: int):
    customer = get_object_or_404(Customer, pk=id)
    if request.method == 'GET':
        return render(request, 'customer/customer-form.html', context={
                'form': CustomerForm(customer.__dict__),
                'action': f'/update/{id}',
                'messages': messages.get_messages(request),
            })
    
    form = CustomerForm(request.POST, instance=customer)
    if not form.is_valid():
        for _, error in form.errors.items():
            messages.add_message(request, messages.ERROR, error)

        return render(request, 'customer/customer-form.html', context={
                'form': form,
                'action': f'/update/{id}',
                'messages': messages.get_messages(request),
            })
    
    form.save()

    return redirect('/customer/')
    