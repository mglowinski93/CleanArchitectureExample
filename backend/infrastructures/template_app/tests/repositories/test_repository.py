import pytest

from apps.template_app.domain.entities import Template as TemplateEntity
from infrastructures.template_app.models import Template as TemplateModel
from infrastructures.template_app.repositories import DjangoTemplateRepository


@pytest.mark.django_db
def test_save(template_entity: TemplateEntity):
    # When
    DjangoTemplateRepository.save(template_entity)

    # Then
    assert template_entity == DjangoTemplateRepository.map_model_to_entity(
        TemplateModel.objects.get(id=template_entity.id)
    )


def test_get(template_model: TemplateModel):
    # When
    entity = DjangoTemplateRepository.get(template_id=template_model.id)

    # Then
    assert entity == DjangoTemplateRepository.map_model_to_entity(template_model)


def test_list(template_model: TemplateModel):
    # When
    entities = DjangoTemplateRepository.list()

    # Then
    assert isinstance(entities, list)
    assert len(entities) == 1
    assert entities[0] == DjangoTemplateRepository.map_model_to_entity(template_model)
