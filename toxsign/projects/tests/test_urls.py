import pytest

from django.urls import reverse, resolve
from django.test import Client

from toxsign.projects.tests.factories import ProjectFactory

pytestmark = pytest.mark.django_db

def test_list():
    assert reverse("projects:index") == "/projects/"
    assert resolve("/projects/").view_name == "projects:index"

def test_details():
    project = ProjectFactory.create()
    assert (
        reverse("projects:detail", kwargs={"prjid": project.tsx_id})
        == f"/projects/{project.tsx_id}/"
    )
    assert resolve(f"/projects/{project.tsx_id}/").view_name == "projects:detail"

def test_update():
    project = ProjectFactory.create()
    assert (
        reverse("projects:project_edit", kwargs={"pk": project.tsx_id})
        == f"/projects/project_edit/{project.id}/"
    )
    assert resolve(f"/projects/project_edit/{project.id}/").view_name == "projects:project_edit"
