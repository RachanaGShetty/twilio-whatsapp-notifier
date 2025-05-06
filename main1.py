from twilio.rest import Client

# Twilio credentials
account_sid = 'TWILIO_SID'
auth_token = 'TWILIO_TOKEN'

# Correctly formatted WhatsApp numbers
whatsapp_from = 'whatsapp:+14155238886'  # Twilio sandbox number
whatsapp_to = 'whatsapp:+919141148516'   # Your verified number

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_=whatsapp_from,
    body='📧 You have a new email notification!',
    to=whatsapp_to
)

print(f'Message sent with SID: {message.sid}')
