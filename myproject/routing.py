from django.urls import path
from myapp import consumers  # Import consumers from `myapp`

websocket_urlpatterns = [
    path('ws/notifications/', consumers.NotificationConsumer.as_asgi()),
]