from django.db import models
from customer.models.enums.lead_state import LeadState


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    number = models.CharField(max_length=15, null=True, blank=True)
    state = models.CharField(choices=LeadState.choices, default=LeadState.NEW, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
