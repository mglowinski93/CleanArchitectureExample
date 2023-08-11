import pytest

from infrastructures.template_app.models import Template as TemplateModel
from infrastructures.template_app.queries import DjangoGetTemplate, DjangoListTemplates
from infrastructures.template_app.queries.templates import map_template_entity_to_dto
from infrastructures.template_app.repositories import DjangoTemplateRepository


@pytest.mark.django_db
def test_get_template_query(template_model: TemplateModel):
    # When
    result = DjangoGetTemplate().query(template_model.id)

    # Then
    assert result == map_template_entity_to_dto(
        DjangoTemplateRepository.map_model_to_entity(template_model)
    )


@pytest.mark.django_db
def test_list_templates_query(template_model: TemplateModel):
    # When
    results = DjangoListTemplates().query()

    # Then
    assert isinstance(results, list)
    assert len(results) == 1
    assert results[0] == map_template_entity_to_dto(
        DjangoTemplateRepository.map_model_to_entity(template_model)
    )
