from django import template
from bootstrap_themes import list_themes

from dashboard.models import Theme

register = template.Library()


@register.assignment_tag
def get_themes():
    return map(list, list_themes())


@register.filter()
def get_user_theme(request):
    try:
        current_user = request.user
        obj = Theme.objects.get(user=current_user.id)
        return obj.theme
    except:
        return 'default'
