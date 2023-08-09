import pytest

from apps.template_app.application.repositories import TemplateRepository
from apps.template_app.application.use_cases.executing_example_business_action import (
    ExecutingExampleBusinessAction,
    ExecutingExampleBusinessActionInputDto,
    ExecutingExampleBusinessActionOutputDto,
)
from apps.template_app.domain.entities import Template


@pytest.fixture()
def input_dto(template: Template) -> ExecutingExampleBusinessActionInputDto:
    return ExecutingExampleBusinessActionInputDto(
        id=template.id,
    )


def test_executing_example_business_action(
    template_repository_mock: TemplateRepository,
    template: Template,
    executing_example_business_action: ExecutingExampleBusinessAction,
    input_dto: ExecutingExampleBusinessActionInputDto,
):
    # When
    executing_example_business_action.execute(input_dto)

    # Then
    template_repository_mock.get.assert_called()
