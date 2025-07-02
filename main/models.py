from django.contrib.auth.models import User
from django.db import models

DB_TYPE_CHOICES = (
    ("postgresql", "PostgreSQL"),
    ("mysql", "MySQL"),
)

class DatabaseConnection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    db_type = models.CharField(max_length=20, choices=DB_TYPE_CHOICES)
    host = models.CharField(max_length=255)
    port = models.IntegerField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)  # <-- Remove encrypt here
    db_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} {self.db_type} {self.db_name}"

class QueryHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    db_conn = models.ForeignKey(DatabaseConnection, on_delete=models.CASCADE)
    nl_query = models.TextField()
    sql_query = models.TextField()
    result = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)