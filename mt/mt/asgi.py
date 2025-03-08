"""
ASGI config for mt project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/stable/howto/deployment/asgi/
"""

import os
=======
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

>>>>>>> bddae2e57bd51d9b3a5c0d1ac075d0ae8df1698d
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mt.settings')

application = get_asgi_application()
