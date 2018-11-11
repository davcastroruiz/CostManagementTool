from models import Project, Field


def save_project(name, owner, email):
    project = Project(name=name, owner=owner, email=email)
    project.save()


def remove_project(_id):
    project = Project.objects.get(id=_id)
    project.delete()


def save_field(name, description):
    field = Field(name=name, description=description)
    field.save()


def remove_field(_id):
    field = Field.objects.get(id=_id)
    field.delete()
