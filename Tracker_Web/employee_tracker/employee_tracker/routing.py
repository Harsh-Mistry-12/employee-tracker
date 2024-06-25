from django.urls import path
from .channels import LogConsumer

websocket_urlpatterns = [
    path('live_log/', LogConsumer.as_asgi()),
]