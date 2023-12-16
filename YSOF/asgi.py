"""
ASGI config for YSOF project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os


from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import Home.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'YSOF.settings')



application = ProtocolTypeRouter({
    # http请求使用这个
    'http': get_asgi_application(),
    # websocket请求使用这个
    'websocket': AuthMiddlewareStack(
        URLRouter(
            Home.routing.websocket_urlpatterns
        )
    ),
})
