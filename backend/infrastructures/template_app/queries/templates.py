from typing import List

from apps.template_app.application.queries.templates import (
    TemplateDto,
    GetTemplate,
    ListTemplates,
)
from apps.template_app.domain.entities import Template as TemplateEntity
from apps.template_app.domain.value_objects import TemplateIdType
from ..repositories.template import DjangoTemplateRepository


class DjangoGetTemplate(GetTemplate):
    def query(self, template_id: TemplateIdType) -> TemplateDto:
        return map_template_entity_to_dto(DjangoTemplateRepository.get(template_id))


class DjangoListTemplates(ListTemplates):
    def query(self) -> List[TemplateDto]:
        return [
            map_template_entity_to_dto(template)
            for template in DjangoTemplateRepository.list()
        ]


def map_template_entity_to_dto(template_entity: TemplateEntity) -> TemplateDto:
    return TemplateDto(
        id=template_entity.id,
        value=template_entity.value,
        timestamp=template_entity.timestamp,
    )
