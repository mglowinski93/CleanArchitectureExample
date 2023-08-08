import abc
from dataclasses import dataclass
from datetime import datetime
from typing import List

from ...domain.value_objects import TemplateIdType


@dataclass
class TemplateDto:
    id: TemplateIdType
    value: str
    timestamp: datetime


class GetTemplate(abc.ABC):
    @abc.abstractmethod
    def query(self, template_id: int) -> TemplateDto:
        pass


class ListTemplates(abc.ABC):
    @abc.abstractmethod
    def query(self) -> List[TemplateDto]:
        pass
