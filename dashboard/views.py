from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncDate
from crm.models import Customer, Interaction, LeadState


def get_lead_data() -> dict[str, list[any]]:
    labels = [key[0] for key in LeadState.choices]
    lead_stage_counts = Customer.objects.values('lead_state')\
        .annotate(count=Count('id'))

    data_dict = {item['lead_state']: item['count'] for item in lead_stage_counts}

    data = [data_dict.get(label, 0) for label in labels]

    return {
        'lead_pipeline_labels': labels,
        'lead_pipeline_data': data,
    }


def get_interactions_over_time_data() -> dict[str, list[any]]:
    interactions_per_day = Interaction.objects.annotate(day=TruncDate('created_at'))\
        .values('day')\
        .annotate(count=Count('id'))\
        .order_by('day')
    
    labels = [item['day'].strftime('%Y-%m-%d') for item in interactions_per_day]
    data = [item['count'] for item in interactions_per_day]

    return {
        'interactions_over_time_labels': labels,
        'interactions_over_time_data': data,
    }


def get_interaction_type_data() -> dict[str, list[any]]:
    interaction_type_counts = Interaction.objects.values('contact_type').annotate(count=Count('id'))

    labels = [Interaction(contact_type=item['contact_type']).get_contact_type_display() for item in interaction_type_counts]
    data = [item['count'] for item in interaction_type_counts]

    return {
        'interactions_types_labels': labels,
        'interactions_types_data': data
    }


def get_recent_customers() -> dict[str, list[any]]:
    new_customers_per_day = Customer.objects.annotate(
        day=TruncDate('created_at')
    )\
    .values('day')\
    .annotate(count=Count('id'))\
    .order_by('day')

    labels = [item['day'].strftime('%Y-%m-%d') for item in new_customers_per_day]
    data = [item['count'] for item in new_customers_per_day]

    return {
        'recent_customers_labels': labels,
        'recent_customers_data': data
    }


def dashboard(request):
    context = dict()

    context.update(get_lead_data())
    context.update(get_interactions_over_time_data())
    context.update(get_interaction_type_data())
    context.update(get_recent_customers())

    return render(request, 'dashboard/index.html', context=context)
