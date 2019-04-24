"""
WSGI config for langsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/var/www/vhosts/LangSite')
sys.path.append('/var/www/vhosts/LangSite/venv/lib/python3.4/site-packages')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'langsite.settings')

application = get_wsgi_application()
