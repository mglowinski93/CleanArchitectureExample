import pytest

from apps.template_app.domain.entities import Template
from apps.template_app.domain.exceptions import ExampleBusinessOperationFailed


def test_example_business_action_raises_exception(
    template: Template,
):
    with pytest.raises(ExampleBusinessOperationFailed):
        template.example_business_action()
