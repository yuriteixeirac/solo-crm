from django.urls import path
from customer.views import detail_customer, list_customers, add_customer


urlpatterns = [
    path('<int:id>/', detail_customer, name='detail-customer'),
    path('add/', add_customer, name='add-customer'),
    path('', list_customers, name='list-customers')
]