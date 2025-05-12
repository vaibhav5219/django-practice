from django.core.management.base import BaseCommand
from confluent_kafka import Consumer, KafkaException # type: ignore
from confluent_kafka import KafkaError # type: ignore
import json
from kafka_zookeeper_app.models import LocationUpdate
import os

class Command(BaseCommand):
    help = "Run kafka consumer to listen for location update"
    
    def handle(self, *args, **options): # type: ignore
        conf = {
            'bootstrap.servers': 'localhost:9092',
            'group.id' : "location_update",
            'auto.offset.reset' : 'earliest',
        }
        consumer = Consumer(conf)
        consumer.subscribe(['location_update'])
        try:
            while True:
                msg = consumer.poll(timeout = 1.0)
                if msg is None:
                    continue
                if msg.error():
                    # if msg.error().code() == KafkaException._PARTITION_EOF:
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        continue
                    else:
                        print(msg.error())
                        break
                data = json.loads(msg.value().decode('utf-8'))
                LocationUpdate.objects.create(
                    latitude = data['lattitude'],
                    longitude = data['longitude'],
                )
                print(f"Received and Save => {data}")
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(e)
        finally:
            consumer.close()
        # return super().handle(*args, **options)
        self.stdout.write(self.style.SUCCESS('Kafka consumer started...'))

    
    