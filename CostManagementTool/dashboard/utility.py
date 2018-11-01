from models import Project


def save_project(name, owner, email):
    project = Project(name=name, owner=owner, email=email)
    project.save()


def remove_project(_id):
    project = Project.objects.get(id=_id)
    project.delete()
