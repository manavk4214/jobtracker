from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'location', 'description', 'date_applied', 'status']
        widgets = {
            'date_applied': forms.DateInput(attrs={'type': 'date'}),
        }

