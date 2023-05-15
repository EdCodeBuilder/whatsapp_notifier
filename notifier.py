from twilio.rest import Client

def send_whatsapp_message(account_sid, auth_token, from_number, to_numbers, message):
    # Configure your Twilio credentials
    client = Client(account_sid, auth_token)

    # Send a WhatsApp message using Twilio
    for to_number in to_numbers:
        message = client.messages \
        .create(
            body=message,
            from_=from_number,
            to=to_number
            )

        print(message.price)
        print(message.price_unit)
        print(message.to)
        print(message.body)
        print('--------------------------------------------------------')