from django.db.models.signals import post_save

import telegram
from .models import SeismicRecord, SeismicNotification


def send_notification(sender, instance, **kwargs):
    notification, _ = SeismicNotification.objects.get_or_create(amplitude=3)

    if instance.amplitude >= notification.amplitude:
        bot = telegram.Bot(token='665012119:AAHpeitpB1cRpSRzFs2r_6gVVZq7B58k6EM')
        bot.send_message(chat_id='@seismic_record', text=f'New seismic record has been recorded with '
                                                         f'amplitude of {instance.amplitude}')


post_save.connect(send_notification, SeismicRecord)