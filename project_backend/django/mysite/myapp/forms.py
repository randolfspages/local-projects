from .models import Task
from django import forms 


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'priority', 'date']