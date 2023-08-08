from dataclasses import dataclass
from uuid import uuid4

from utils import get_current_utc_timestamp
from ..repositories import TemplateRepository
from ...domain.entities import Template


@dataclass
class CreatingTemplateInputDto:
    value: str


class CreatingTemplate:
    def __init__(self, repository: TemplateRepository):
        self.repository = repository

    def execute(self, input_data: CreatingTemplateInputDto) -> None:
        self.repository.save(
            Template(
                id=uuid4(),
                value=input_data.value,
                timestamp=get_current_utc_timestamp(),
            )
        )
