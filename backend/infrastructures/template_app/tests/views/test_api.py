import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.template_app.tests.factories import fake_template_id, fake_template_value
from infrastructures.template_app.models import Template as TemplateModel


def test_list_templates_view_returns_200_status_code(
    api_client: APIClient, template_model: TemplateModel
):
    response = api_client.get(reverse(viewname="templates:template-list"))

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1


def test_get_templates_view_return_data_when_template_exists(
    api_client: APIClient, template_model: TemplateModel
):
    response = api_client.get(
        reverse(viewname="templates:template-detail", args=[template_model.id])
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == str(template_model.id)


@pytest.mark.django_db
def test_get_templates_view_return_404_status_code_when_template_doesnt_exist(
    api_client: APIClient,
):
    response = api_client.get(
        reverse(viewname="templates:template-detail", args=[fake_template_id()])
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_create_templates_view_return_201_status_code(
    api_client: APIClient,
):
    response = api_client.post(
        reverse(
            viewname="templates:template-list",
        ),
        data={
            "value": fake_template_value(),
        },
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_execute_example_business_action_returns_400_status_code(
    api_client: APIClient, template_model: TemplateModel
):
    response = api_client.post(
        reverse(
            viewname="templates:template-execute-example-business-action",
            args=[template_model.id],
        )
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
