from datetime import datetime

from ..exceptions import ExampleBusinessOperationFailed
from ..value_objects import TemplateIdType


class Template:
    """
    Allocate here business logic and high-level rules that are related to this entity.
    """

    def __init__(self, id: TemplateIdType, value: str, timestamp: datetime):
        self.id = id
        self.value = value
        self.timestamp = timestamp

    def example_business_action(self):
        if True:  # Complex business condition check here.
            raise ExampleBusinessOperationFailed  # Oh no, business conditions are not met, action can't be proceeded.
