from django.views.generic import TemplateView
from rest_framework.generics import ListCreateAPIView
from .models import SeismicRecord
from .serializers import SeismicRecordSerializer


class SeismicRecordView(ListCreateAPIView):

    queryset = SeismicRecord.objects.all()
    serializer_class = SeismicRecordSerializer


class ResultsView(TemplateView):

    template_name = 'main.html'
