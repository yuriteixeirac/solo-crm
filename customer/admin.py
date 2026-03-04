from django.contrib import admin
from customer.models import Customer, Interaction, Note


admin.site.register(Customer)
admin.site.register(Interaction)
admin.site.register(Note)
