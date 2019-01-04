from django.contrib import admin
from solo.admin import SingletonModelAdmin
from earthquake_collector.models import SeismicNotification

admin.site.register(SeismicNotification, SingletonModelAdmin)
