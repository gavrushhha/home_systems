import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='parsed_data_queue')

def send_to_db_and_rabbitmq(data):
    channel.basic_publish(exchange='', routing_key='parsed_data_queue', body=json.dumps(data))
    print(f" [x] Sent {data}")

if __name__ == '__main__':
    send_to_db_and_rabbitmq({
        'url': 'https://test.com',
        'name': 'Fal Fakken',
        'parsed_info': {
            'title': 'Primer tests',
            'meta_description': 'HIIIIII!'
        }
    })
    connection.close()
