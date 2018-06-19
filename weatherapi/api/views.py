from rest_framework.generics import ListAPIView
from .serializers import OutputDataSerializer, InputDataSerializer
from ..models import OutputData, InputData


class OutputDataView(ListAPIView):
    serializer_class = OutputDataSerializer
    queryset = OutputData.objects.all()


class InputDataView(ListAPIView):
    serializer_class = InputDataSerializer
    queryset = InputData.objects.all()
