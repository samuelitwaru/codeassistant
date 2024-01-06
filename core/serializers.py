from rest_framework import serializers

from core.utils import TEMPLATE_OPTIONS
from .models import Model, Field, Template



# Serializers define the API representation.
class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'

class ModelSerializer(serializers.ModelSerializer):
    fields = FieldSerializer(many=True, source='field_set')
    class Meta:
        model = Model
        fields = '__all__'

class TemplateSerializer(serializers.Serializer):
    content = serializers.CharField()

    class Meta:
        model = Template
        fields = '__all__'


class GenerateModelCodeSerailizer(serializers.Serializer):
    template = serializers.ChoiceField(choices=tuple(TEMPLATE_OPTIONS))

    class Meta:
        model = Template
        fields = '__all__'
