import os

DEBUG = True

BROKER = 'amqp://127.0.0.1:5672'

NOTIFIER_HOST = os.environ.get('NOTIFIER_SERVICE_HOST', 'localhost')
NOTIFIER_PORT = int(os.environ.get('NOTIFIER_SERVICE_PORT', 3000))
NOTIFIER_URL = os.environ.get('NOTIFIER_URL', '')

RABBITMQ_HOST = os.environ.get('RABBITMQ_PORT_5672_TCP_ADDR', 'localhost')
RABBITMQ_PORT = int(os.environ.get('RABBITMQ_PORT_5672_TCP_HOST', 5672))
