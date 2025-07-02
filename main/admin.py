from django.contrib import admin
from .models import DatabaseConnection, QueryHistory

admin.site.register(DatabaseConnection)
admin.site.register(QueryHistory)