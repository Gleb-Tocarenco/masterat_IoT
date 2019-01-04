from django.urls import path
from .views import SeismicRecordView, ResultsView


urlpatterns = [
    path('seismic-records/', SeismicRecordView.as_view()),
    path('', ResultsView.as_view())
]
