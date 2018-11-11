from django import template

register = template.Library()


@register.simple_tag
def get_private_attribute(model_instance, attrib_name):
    return model_instance[attrib_name]


@register.filter()
def integer(var):
    try:
        var = int(var)
    except ValueError:
        pass

    return var


@register.filter()
def sort_by_key(items_r):
    items_r = dict(items_r)
    return sorted(items_r.items())
