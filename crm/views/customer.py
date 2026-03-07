from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from crm.models import Customer, Interaction
from crm.forms import CustomerForm


def detail_customer(request, id: int):
    customer = get_object_or_404(Customer, pk=id)
    interactions = Interaction.objects.filter(customer=customer)

    return render(request, 'customer/customer-detail.html', context={
        'customer': customer,
        'interactions': interactions
    })


def list_customers(request):
    query = request.GET.get('q', '')
    
    if not query:
        customers = Customer.objects.all()
        return render(request, 'customer/customer-list.html', context={
            'method': 'GET',
            'customers': customers
        })
    
    customers = Customer.objects.filter(
        Q(name__icontains=query) |\
        Q(number__icontains=query) |\
        Q(email__icontains=query) 
    )

    return render(request, 'customer/customer-list.html', context={
        'method': 'GET',
        'customers': customers
    })


def add_customer(request):
    if request.method == 'GET':
        return render(request, 'form.html', context={
            'action': '/customer/add/',
            'method': 'POST',
            'form': CustomerForm()
        })

    form = CustomerForm(request.POST)
    
    if not form.is_valid():
        for _, error in form.errors.items():
            messages.add_message(request, messages.ERROR, error)

        return render(request, 'customer/customer-form.html', context={
            'action': '/customer/add/',
            'form': CustomerForm(),
            'method': 'POST',
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
    form = CustomerForm(instance=customer)

    if request.method == 'GET':
        return render(request, 'customer/customer-form.html', context={
                'form': form,
                'action': f'/customer/update/{id}/',
                'method': 'POST',
                'messages': messages.get_messages(request),
            })
    
    form = CustomerForm(request.POST, instance=customer)
    if not form.is_valid():
        for _, error in form.errors.items():
            messages.add_message(request, messages.ERROR, error)

        return render(request, 'customer/customer-form.html', context={
                'form': form,
                'action': f'/customer/update/{id}/',
                'method': 'POST',
                'messages': messages.get_messages(request),
            })
    
    form.save()

    return redirect('/customer/')
    