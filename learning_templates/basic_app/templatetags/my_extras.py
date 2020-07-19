from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    This cut all the values of 'arg' from the strings

    """
    return value.replace(arg, '')

# register.filter('cut', cut)
