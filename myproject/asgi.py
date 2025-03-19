import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path  # Add this import
from myapp import consumers  # Import consumers from `myapp`

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter([
        path("ws/notifications/", consumers.NotificationConsumer.as_asgi()),
    ]),
})