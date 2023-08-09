import pytest
from unittest.mock import Mock


from apps.template_app.application.repositories import TemplateRepository

from apps.template_app.domain.entities import Template
from .factories import TemplateFactory


@pytest.fixture
def template() -> Template:
    return TemplateFactory()


@pytest.fixture
def template_repository_mock() -> Mock:
    return Mock(spec_set=TemplateRepository)
