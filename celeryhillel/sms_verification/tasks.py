from celery import shared_task
from django.conf import settings
from twilio.rest import Client

client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)


@shared_task
def send_sms(receiver, message):
    message = client.messages.create(from_="+13344781120", body=message, to=receiver)

    print(message.sid)
    return message.sid
