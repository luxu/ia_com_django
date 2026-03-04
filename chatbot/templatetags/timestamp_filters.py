from django import template
from datetime import datetime
from django.utils import timezone

register = template.Library()


@register.filter
def timestamp_to_date(value):
    try:
        return datetime.fromtimestamp(int(value), tz=timezone.get_current_timezone())
    except:
        return None
