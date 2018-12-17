from rest_framework.serializers import ModelSerializer
from .models import SeismicRecord


class SeismicRecordSerializer(ModelSerializer):

    class Meta:
        model = SeismicRecord
        exclude = ('added_at', )
