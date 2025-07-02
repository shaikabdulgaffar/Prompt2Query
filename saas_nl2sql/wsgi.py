import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'saas_nl2sql.settings')
application = get_wsgi_application()