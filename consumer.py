import pika
from models_rabbit import Contact 

def fake_send_email(contact):
    print(f"Email sent to {contact.full_name} at {contact.email}")

def callback(ch, method, properties, body):
    contact_id = body.decode()
    contact = Contact.objects.get(id=contact_id)
    
    fake_send_email(contact)
    
    contact.email_sent = True
    contact.save()
    
    print(f"Processed {contact}")

def start_consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters('5672'))
    channel = connection.channel()
    
    channel.queue_declare(queue='email_queue')
    channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    start_consumer()
