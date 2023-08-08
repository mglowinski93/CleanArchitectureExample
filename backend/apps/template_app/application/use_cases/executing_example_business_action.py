from datetime import datetime
from dataclasses import dataclass

from utils import get_current_utc_timestamp
from ..repositories import TemplateRepository
from ...domain.value_objects import TemplateIdType


@dataclass
class ExecutingExampleBusinessActionInputDto:
    id: TemplateIdType


@dataclass
class ExecutingExampleBusinessActionOutputDto:
    id: TemplateIdType
    timestamp: datetime


class ExecutingExampleBusinessAction:
    def __init__(
        self,
        repository: TemplateRepository,
    ):
        self.repository = repository

    def execute(
        self, input_data: ExecutingExampleBusinessActionInputDto
    ) -> ExecutingExampleBusinessActionOutputDto:
        template = self.repository.get(input_data.id)
        template.example_business_action()

        return ExecutingExampleBusinessActionOutputDto(
            id=template.id,
            timestamp=get_current_utc_timestamp(),
        )
