from django.urls import path
from .views import SeismicRecordView


urlpatterns = [
    path('seismic-records/', SeismicRecordView.as_view())
]
