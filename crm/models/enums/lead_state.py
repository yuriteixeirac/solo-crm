from django.db import models


class LeadState(models.TextChoices):
    NEW = ('new', 'New')
    CONTACTED = ('contacted', 'Contacted')
    PROPOSAL = ('proposal', 'Proposal sent')
    WON = ('won', 'Closed won')
    LOST = ('lost', 'Closed lost')
