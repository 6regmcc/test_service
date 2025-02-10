import pika

def send():
    credentials = pika.PlainCredentials('default_user_76OfnLbsBcbM1bz9WgU', 'fqg-oAhmS8jJG0HCxib6Ub_DBFQ0IEcS')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='hello-world', credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
    print(" [x] Sent 'Hello World!'")
    connection.close()


