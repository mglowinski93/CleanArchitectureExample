import pytest
from unittest.mock import Mock

from apps.template_app.application.use_cases.creating_template import CreatingTemplate
from apps.template_app.application.use_cases.executing_example_business_action import (
    ExecutingExampleBusinessAction,
)


@pytest.fixture
def creating_template(template_repository_mock: Mock) -> CreatingTemplate:
    return CreatingTemplate(template_repository_mock)


@pytest.fixture
def executing_example_business_action(
    template_repository_mock: Mock,
) -> ExecutingExampleBusinessAction:
    return ExecutingExampleBusinessAction(template_repository_mock)
