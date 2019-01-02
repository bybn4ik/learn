# -*- coding: utf-8 -*-
import pytest
from new_contact_group import New_contact_group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_new_contact(app):
    app.login(password="secret", username="admin")
    app.created_contact(New_contact_group(firstname ="Мышин", middlename ="Виссарионий",
                                              lastname= "Альбертович", address = "Болотная улица",
                                              homephone = "89589765421", mobile = "89458966525",
                                              email = "bred@yandex.ru",
                                              bday="", bmonth="", byear="1987"))
    app.logout()


def test_new_2_contact(app):
    app.login(password="secret", username="admin")
    app.created_2contact(New_contact_group(firstname ="Хрящин", middlename ="Петро",
                                              lastname= "Васильевич", address = "Парнокопытная улица",
                                              homephone = "89589762698", mobile = "89458966684",
                                              email = "хрунов@yandex.ru",
                                              bday = "", bmonth = "", byear = "1993"))
    app.logout()
