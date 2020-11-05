"""Test views in pur_beurre app"""
from django.test import Client

from pytest import mark

from foodsubstitute.models import Question, Choice

import pdb

@mark.django_db
def test_detail_product():

    client = Client()
    response = client.get("/foodsubstitute/1")
    # quest = response.context["question"]

    # assert quest.question_text == "What's new"
    assert response.status_code == 301
    # assert response.templates.name == "foodsubstitute/detail.html"

@mark.django_db
def test_index():

    client = Client()
    response = client.get("/foodsubstitute/")

    assert response.status_code == 200
    # assert response.templates.name == "foodsubstitute/index.html"
