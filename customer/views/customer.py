from customer.models import Customer
from django.http.response import HttpResponse


def get_all(request):
    return HttpResponse(Customer.objects.all())
