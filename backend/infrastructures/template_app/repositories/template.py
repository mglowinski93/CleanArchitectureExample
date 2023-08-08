from apps.template_app.application.repositories import TemplateRepository
from apps.template_app.domain.entities import Template as TemplateEntity
from apps.template_app.domain.value_objects import TemplateIdType
from ..models import Template as TemplateModel


class DjangoTemplateRepository(TemplateRepository):
    @staticmethod
    def map_model_to_entity(model: TemplateModel) -> TemplateEntity:
        return TemplateEntity(
            id=model.id,
            value=model.value,
            timestamp=model.timestamp,
        )

    @staticmethod
    def map_entity_to_model(entity: TemplateEntity) -> TemplateModel:
        return TemplateModel(
            id=entity.id,
            value=entity.value,
            timestamp=entity.timestamp,
        )

    @classmethod
    def save(cls, template: TemplateEntity):
        cls.map_entity_to_model(template).save()

    @classmethod
    def get(cls, template_id: TemplateIdType) -> TemplateEntity:
        return cls.map_model_to_entity(TemplateModel.objects.get(id=template_id))

    @classmethod
    def list(cls) -> list[TemplateEntity]:
        return [
            cls.map_model_to_entity(template)
            for template in TemplateModel.objects.all()
        ]
