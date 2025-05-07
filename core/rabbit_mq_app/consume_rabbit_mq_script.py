import pika
import pandas as pd
import json
import uuid

def generateExcel(message):
    message = json.loads(message)
    df = pd.DataFrame(message)
    df.to_excel(f"output_{uuid.uuid4()}.xlsx", index=False)

def callback(ch, method, properties, body):
    print(ch, method, properties, body)
    

''' Binding callback to consume rabbitmq '''
params = pika.URLParameters('amqps://zzwbkujc:JNHuHbV1fDGgmlXsv_bExuCYGaNobHBR@puffin.rmq2.cloudamqp.com/zzwbkujc') # Got it from https://api.cloudamqp.com/console/b45f2a21-346f-4b35-b851-3e6465c51800/details
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue="my_queue")
channel.basic_consume(queue="my_queue", on_message_callback=callback, auto_ack=True)
print("consumer started :")
channel.start_consuming()