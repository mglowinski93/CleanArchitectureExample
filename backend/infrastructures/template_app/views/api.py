from http import HTTPStatus

from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from apps.template_app.application.use_cases import (
    CreatingTemplate,
    CreatingTemplateInputDto,
    ExecutingExampleBusinessAction,
    ExecutingExampleBusinessActionInputDto,
    ExecutingExampleBusinessActionOutputDto,
)
from apps.template_app.domain.exceptions import ExampleBusinessOperationFailed
from apps.template_app.application.queries import TemplateDto
from apps.template_app.domain.value_objects import TemplateIdType
from .serializers import (
    TemplateCreateSerializer,
    TemplateDtoSerializer,
    ExecutingExampleBusinessActionOutputDto,
)
from ..models import Template as TemplateModel
from ..queries import DjangoGetTemplate, DjangoListTemplates
from ..repositories import DjangoTemplateRepository


repository = DjangoTemplateRepository()


class TemplateViewSet(
    ViewSet,
):
    serializer_class = TemplateDtoSerializer

    def list(self, request):
        results: list[TemplateDto] = DjangoListTemplates().query()

        return Response(self.serializer_class(results, many=True).data)

    def retrieve(self, request, pk: TemplateIdType):
        try:
            template: TemplateDto = DjangoGetTemplate().query(template_id=pk)
        except TemplateModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(self.serializer_class(template).data)

    def create(self, request):
        serializer = TemplateCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        CreatingTemplate(repository).execute(
            CreatingTemplateInputDto(
                value=serializer.validated_data["value"],
            )
        )

        return Response(
            status=status.HTTP_201_CREATED,
        )

    @action(methods=["POST"], detail=True, url_path="execute-example-business-action")
    def execute_example_business_action(self, request, pk: TemplateIdType):
        try:
            result: ExecutingExampleBusinessActionOutputDto = (
                ExecutingExampleBusinessAction(repository).execute(
                    ExecutingExampleBusinessActionInputDto(
                        id=pk,
                    )
                )
            )
        except ExampleBusinessOperationFailed:
            return Response(status=HTTPStatus.BAD_REQUEST)
        except TemplateModel.DoesNotExist:
            return Response(status=HTTPStatus.NOT_FOUND)

        return Response(
            status=HTTPStatus.OK, data=ExecutingExampleBusinessActionOutputDto(result)
        )
