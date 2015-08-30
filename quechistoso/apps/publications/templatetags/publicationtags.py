from django import template

register = template.Library()

@register.filter
def owner(value):
    return 'Anónimo' if value is None else value