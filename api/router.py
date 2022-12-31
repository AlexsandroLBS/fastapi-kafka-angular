import json
from fastapi import APIRouter
from api.schema import Notification
from api.config import loop, KAFKA_BOOTSTRAP_SERVERS, KAFKA_CONSUMER_GROUP, KAFKA_TOPIC
from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
from api.processing import Process
route = APIRouter()


@route.post('/send_requisition')
async def send(request: Notification):
    producer = AIOKafkaProducer(
        loop=loop, bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
    await producer.start()
    try:
        print(f'Sendding request with value: {request}')
        value_json = json.dumps(request.__dict__).encode('utf-8')
        await producer.send_and_wait(topic=KAFKA_TOPIC, value=value_json)
    finally:
        await producer.stop()


async def consume():
    consumer = AIOKafkaConsumer(KAFKA_TOPIC, loop=loop,
                                bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS, group_id=KAFKA_CONSUMER_GROUP)
    await consumer.start()
    process = Process()
    try:
        async for req in consumer:
            print(json.loads(req.value))
            process.sendDatabase(json.loads(req.value))
    finally:
        await consumer.stop()