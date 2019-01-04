from django.db.models.signals import post_save

from .models import SeismicRecord, SeismicNotification


def send_notification(sender, instance, **kwargs):
    notification, _ = SeismicNotification.objects.get_or_create(amplitude=5)

    if instance.amplitude >= notification.amplitude:
        print('send notification')


post_save.connect(send_notification, SeismicRecord)