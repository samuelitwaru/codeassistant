from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, action
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Model, Field, Template
from .serializers import GenerateModelCodeSerailizer, ModelSerializer, FieldSerializer, TemplateSerializer
from .utils import TEMPLATE_OPTIONS, jinja_env, render_jinja_from_file


# Create your views here.
class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects
    serializer_class = ModelSerializer
    
    @action(detail=True, methods=['POST', 'GET'], name='generate_model_code', url_path=r'generate_model_code', serializer_class=GenerateModelCodeSerailizer)
    def generate_model_code(self, request, pk, *args, **kwargs):
        if request.method == 'GET':
            return Response({}, status=status.HTTP_200_OK)
        model = get_object_or_404(Model, pk=pk)
        
        template = request.POST.get('template')
        file = TEMPLATE_OPTIONS[template]
        template = render_jinja_from_file(
            file,
            model=model
            )
        lines = template.split('\n')
        for line in lines:
            if line.strip(): print(line)
        template = Template.objects.create(content=template)
        data = TemplateSerializer(template).data
        return Response(data, status=status.HTTP_200_OK)


class FieldViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer 


@api_view(['POST'])
def generate_model_list_template(request):
    data = {}
    return Response(data, status=status.HTTP_200_OKTTP)