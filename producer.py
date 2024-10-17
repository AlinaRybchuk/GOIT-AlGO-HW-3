import pika 
from faker import Faker
from models_rabbit import Contact 

fake = Faker()

def create_contacts(num_contacts):
    contacts = []
    for _ in range(num_contacts):
        contact = Contact(
            full_name=fake.name(),
            email=fake.email()
        )
        contact.save()
        contacts.append(contact)
    return contacts

def send_to_queue(contacts):
    connection = pika.BlockingConnection(pika.ConnectionParameters('5672'))
    channel = connection.channel()
    
    channel.queue_declare(queue='email_queue')
    
    for contact in contacts:
        channel.basic_publish(
            exchange='',
            routing_key='email_queue',
            body=str(contact.id) 
        )
        print(f"Sent {contact}")

    connection.close()

if __name__ == '__main__':
    num_contacts = 10 
    contacts = create_contacts(num_contacts)
    send_to_queue(contacts)
