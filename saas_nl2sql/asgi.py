import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'saas_nl2sql.settings')
application = get_asgi_application()