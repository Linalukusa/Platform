from django import forms
from .models import Research
from django.core.exceptions import ValidationError
from bootstrap_datepicker_plus.widgets import DateTimePickerInput


class ResearchCreationForm(forms.ModelForm):
    class Meta:
        model = Research
        fields = ['title', 'leadresearcher', 'publisher','city','website','researchfile',
        'email','startdate','enddate','description','collab','funding']
        widgets = {
        'startdate': DateTimePickerInput(),
        'enddate':DateTimePickerInput(),
    }
        


class ResearchUpdateForm(forms.ModelForm):
    class Meta:
        model = Research
        fields = ['title', 'leadresearcher', 'publisher','city','website','researchfile',
        'email','startdate','enddate','description','collab','funding']
        widgets = {
        'startdate':DateTimePickerInput(),
        'enddate':DateTimePickerInput(),
    }
