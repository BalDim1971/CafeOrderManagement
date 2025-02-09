from django import template

register = template.Library()


@register.simple_tag()
def mediapath(val: str) -> str:
    if val:
        return f'/media/{val}'
    
    return '#'


@register.filter()
def mymedia(val: str) -> str:
    if val:
        return f'/media/{val}'
    
    return '#'
