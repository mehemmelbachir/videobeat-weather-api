from rest_framework.serializers import ModelSerializer
from ..models import InputData, OutputData


class OutputDataSerializer(ModelSerializer):

    class Meta:
        model = OutputData
        fields = ['date_time',
                  'avg_temperature',
                  'avg_wind_speed',
                  'direction_in_space']
        read_only_fields = ['date_time',
                            'avg_temperature',
                            'avg_wind_speed',
                            'direction_in_space']



class InputDataSerializer(ModelSerializer):
    class Meta:
        model = InputData
        fields = ['date',
                  'time',
                  'latitude',
                  'longitude',
                  'hight_ug',
                  'temperature',
                  'wind_speed',
                  'wind_vector_direction']

        read_only_fields = ['date',
                  'time',
                  'latitude',
                  'longitude',
                  'hight_ug',
                  'temperature',
                  'wind_speed',
                  'wind_vector_direction']

