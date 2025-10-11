from django import template

register = template.Library()

def first_five_upper(value):
    result = value[:3]
    return result

register.filter('ffu',first_five_upper)