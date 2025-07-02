from django import forms
from .models import DatabaseConnection

class DatabaseConnectionForm(forms.ModelForm):
    class Meta:
        model = DatabaseConnection
        fields = ['db_type', 'host', 'port', 'username', 'password', 'db_name']
        labels = {
            'db_type': 'Database Type', 'db_name': 'Database Name'
        }

class NLQueryForm(forms.Form):
    nl_query = forms.CharField(widget=forms.Textarea(attrs={"rows":2, "placeholder": "Ask in natural language..."}))