from abc import ABC, abstractmethod

from ...domain.entities import Template
from ...domain.value_objects import TemplateIdType


class TemplateRepository(ABC):
    @classmethod
    @abstractmethod
    def save(cls, template: Template):
        pass

    @classmethod
    @abstractmethod
    def get(cls, template_id: TemplateIdType) -> Template:
        pass

    @classmethod
    @abstractmethod
    def list(cls) -> list[Template]:
        pass
