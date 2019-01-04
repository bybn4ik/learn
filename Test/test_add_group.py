# -*- coding: utf-8 -*-
import pytest
from Model.group import Group
from Fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Старая", header="Хрень", footer="НеВерная"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Новая", header="", footer=""))
    app.session.logout(as)