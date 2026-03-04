from django.db import models


class LeadState(models.TextChoices):
    NEW = ('new', 'New')
    ATTEMPTED_TO_CONTACT = ('attempted', 'Attempted to Contact')
    CONTACTED = ('contacted', 'Contacted')
    QUALIFIED = ('qualified', 'Qualified')
    DEMO = ('demo', 'Demo sent')
    PROPOSAL = ('proposal', 'Proposal sent')
    NEGOTIATING = ('negotiating', 'Negotiating')
    CLOSED_WON = ('closed won', 'Closed won')
    CLOSED_LOST = ('closed lost', 'Closed lost')
