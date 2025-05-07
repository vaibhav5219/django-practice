import pika
import json

def publish_message(mess):
    params = pika.URLParameters('amqps://zzwbkujc:JNHuHbV1fDGgmlXsv_bExuCYGaNobHBR@puffin.rmq2.cloudamqp.com/zzwbkujc') # Got it from https://api.cloudamqp.com/console/b45f2a21-346f-4b35-b851-3e6465c51800/details
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue="my_queue")
    message = json.dumps(mess)
    channel.basic_publish(
        exchange='',
        routing_key="my_queue",
        body=message,
    )
    print(f"Message Published => {message}")
    connection.close()