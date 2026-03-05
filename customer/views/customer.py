from customer.models import Customer, Interaction
from django.shortcuts import render, redirect, get_object_or_404
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
        return render(request, 'customer/add-customer.html', context={
            'form': CustomerForm()
        })

    form = CustomerForm(request.POST)
    
    if not form.is_valid():
        return render(request, 'customer/add-customer.html', context={
            'form': CustomerForm()
        })

    # Validar número dentro do forms

    customer = form.save(commit=False)
    customer.name = customer.name.title()

    customer.save()

    return redirect('/customer')