import datetime

from django import forms
from django.core.exceptions import ValidationError
from table.models import Table

class Form(forms.Form):
    fields = [tuple([f.name, f.name]) for f in Table._meta.get_fields() if f.name!='date']
    col = forms.CharField(label='Column to filter', widget=forms.Select(choices=fields))
    operations = [('>','>'), ('=','='), ('<','<')]
    statement = forms.CharField(label='Operation', widget=forms.Select(choices=operations))
    value = forms.CharField(label='value')
    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        self.fields['value'].required = False