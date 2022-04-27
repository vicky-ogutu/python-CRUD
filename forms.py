from dataclasses import field, fields
from pyexpat import model
from django import forms
from CRUD_operation.models import main_clientsModel

class client_form(forms.ModelForm):

    class Meta:
        model=main_clientsModel
        fields=('client_id', 'client_name', 'client_county', 'client_age',)

    
        