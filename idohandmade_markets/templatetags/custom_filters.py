# idohandmade_markets/templatetags/custom_filters.py
from django import template

register = template.Library()


@register.filter
def number_to_words(value):
    num_words = [
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
    ]
    try:
        return num_words[int(value) - 1]
    except (IndexError, ValueError):
        return value
