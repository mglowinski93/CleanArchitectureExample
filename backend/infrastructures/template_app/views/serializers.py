from rest_framework import serializers


class TemplateDtoSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    value = serializers.CharField()
    timestamp = serializers.DateTimeField()


class TemplateCreateSerializer(serializers.Serializer):
    value = serializers.CharField(min_length=1)


class ExecutingExampleBusinessActionOutputDto(serializers.Serializer):
    id = serializers.UUIDField()
    timestamp = serializers.DateTimeField()
