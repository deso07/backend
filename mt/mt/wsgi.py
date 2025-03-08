"""
WSGI config for mt project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/stable/howto/deployment/wsgi/
"""

import os
=======
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

>>>>>>> bddae2e57bd51d9b3a5c0d1ac075d0ae8df1698d
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mt.settings')

application = get_wsgi_application()
