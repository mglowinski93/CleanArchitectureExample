import pytest

from apps.template_app.application.repositories import TemplateRepository
from apps.template_app.application.use_cases.creating_template import (
    CreatingTemplate,
    CreatingTemplateInputDto,
)
from ...factories import fake_template_value


@pytest.fixture()
def input_dto() -> CreatingTemplateInputDto:
    return CreatingTemplateInputDto(
        value=fake_template_value(),
    )


def test_create_template(
    template_repository_mock: TemplateRepository,
    creating_template: CreatingTemplate,
    input_dto: CreatingTemplateInputDto,
):
    # When
    creating_template.execute(input_dto)

    # Then
    template_repository_mock.save.assert_called()
