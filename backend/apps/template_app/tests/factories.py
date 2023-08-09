from datetime import datetime

import factory
from faker import Faker

from apps.template_app.domain.entities import Template


fake = Faker()


class TemplateFactory(factory.Factory):
    class Meta:
        model = Template

    id = factory.Faker("uuid4")
    value = factory.Faker("sentence")
    timestamp = factory.LazyFunction(datetime.now)


def fake_template_value() -> str:
    return fake.pystr(min_chars=1, max_chars=100)
