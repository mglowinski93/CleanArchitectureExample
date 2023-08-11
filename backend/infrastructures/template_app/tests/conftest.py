import pytest

from apps.template_app.tests.conftest import (
    template_entity,  # Import template entity fixture required for tests.
)
from infrastructures.template_app.models import Template as TemplateModel
from .factories import TemplateModelFactory


@pytest.fixture
def template_model(db) -> TemplateModel:
    return TemplateModelFactory.create()
