from django.db import models
from crm.models.enums.contact_type import ContactType


class Interaction(models.Model):
    class Meta:
        ordering = ['-created_at']

        
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    contact_type = models.CharField(choices=ContactType.choices, max_length=7)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.customer.name}: {self.contact_type} at {self.created_at}'
