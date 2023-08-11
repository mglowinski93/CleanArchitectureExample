from uuid import uuid4

import factory
from faker import Faker

from infrastructures.template_app.models import Template as TemplateModel
from utils import get_current_utc_timestamp


fake = Faker()


class TemplateModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TemplateModel

    id = factory.LazyFunction(uuid4)
    value = factory.Faker("sentence")
    timestamp = factory.LazyFunction(get_current_utc_timestamp)
