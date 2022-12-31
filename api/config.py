import asyncio

#environment variables
KAFKA_BOOTSTRAP_SERVERS= "kafka:9092"
KAFKA_TOPIC="kafka"
KAFKA_CONSUMER_GROUP="group-id"
loop = asyncio.get_event_loop()

db_config = "dbname=db user=docker password=docker host=localhost port=5432"