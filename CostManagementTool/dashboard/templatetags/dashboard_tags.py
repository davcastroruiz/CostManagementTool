from django import template
from bootstrap_themes import list_themes

from dashboard.models import Theme, Project, Field

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
        theme_ = Theme(user=request.user, theme='default')
        theme_.save()
        return 'default'


@register.simple_tag
def projects():
    return Project.objects.all()


@register.assignment_tag
def fields():
    return Field.objects.all()


@register.filter()
def assigned(field_id, project):
    return project.fields.filter(id=field_id).exists()
