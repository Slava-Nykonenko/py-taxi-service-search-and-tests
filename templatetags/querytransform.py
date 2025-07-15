from django import template

register = template.Library()

@register.simple_tag
def querytransform(request, **kwargs):
    updated = request.GET.copy()
    for k, y in kwargs.items():
        if y is not None:
            updated[k] = y
        else:
            updated.pop(k, 0)
    return updated.urlencode()
