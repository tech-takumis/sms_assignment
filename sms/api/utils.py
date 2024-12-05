from twilio.rest import Client
from django.conf import settings



def send_message(to_phone_number, message_body):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    personalize_message = f"Congratulations {to_phone_number} - {message_body}"

    try:
        message = client.messages.create(
            to=to_phone_number,
            from_=settings.TWILIO_PHONE_NUMBER,
            body=personalize_message  # Ensure this is used
        )
        print(f"Message sent successfully: SID={message.sid}")  # Debug log
        return message.sid
    except Exception as e:
        print(f"Twilio error: {e}")  # Debug log
        raise ValueError(f'Twilio error: {e}')
