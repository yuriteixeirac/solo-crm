from django.urls import path
from customer.views import get_all


urlpatterns = [
    path('', get_all, name='get_all')
]