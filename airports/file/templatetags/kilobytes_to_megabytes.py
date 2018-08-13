from django import template
import re

register = template.Library()

@register.filter
def kilobytes_to_megabytes(value):
    print (value * 0.000001)


    return '{0:.2f}'.format(value * 0.000001)
