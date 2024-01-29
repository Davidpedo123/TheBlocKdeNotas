import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from App import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BlockDeNotas.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter([
        path("ws/some_path/", consumers.MyConsumer.as_asgi()),
    ]),
})
