import pytest

from django.urls import reverse, resolve
from django.test import Client

from toxsign.projects.tests.factories import ProjectFactory

pytestmark = pytest.mark.django_db

def test_list():
    assert reverse("projects:index") == "/projects/"
    assert resolve("/projects/").view_name == "projects:index"
    project = ProjectFactory.create()
    client = Client()
    response = client.get(reverse('projects:index'))
    projects = response.context['project_list']
    assert len(projects) == 1
    new_project = projects[0]
    assert new_project.name == project.name

def test_details():
    project = ProjectFactory.create()
    assert (
        reverse("projects:detail", kwargs={"prjid": project.tsx_id})
        == f"/projects/{project.tsx_id}/"
    )
    assert resolve(f"/projects/{project.tsx_id}/").view_name == "projects:detail"
    client = Client()
    response = client.get(reverse("projects:detail", kwargs={"prjid": project.tsx_id}))
    response_project = projects = response.context['project']
    assert project == response_project
