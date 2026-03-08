from django.urls import path
from crm.views import *


urlpatterns = [
    path('customer/delete/<int:id>/', delete_customer, name='delete-customer'),
    path('customer/update/<int:id>/', update_customer, name='update-customer'),
    path('customer/<int:id>/', detail_customer, name='detail-customer'),
    path('customer/<int:id>/interaction/add/', add_interaction, name='add-interaction'),
    path('customer/add/', add_customer, name='add-customer'),
    path('customer/', list_customers, name='list-customers'),
    path('customer/csv/', get_customers_csv, name='get-customers-csv'),
]