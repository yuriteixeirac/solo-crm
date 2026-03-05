from django.urls import path
from customer.views import *


urlpatterns = [
    path('delete/<int:id>', delete_customer, name='delete-customer'),
    path('update/<int:id>', update_customer, name='update-customer'),
    path('<int:id>/', detail_customer, name='detail-customer'),
    path('add/', add_customer, name='add-customer'),
    path('', list_customers, name='list-customers'),
]