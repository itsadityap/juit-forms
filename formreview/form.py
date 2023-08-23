from django import forms
from selfappraisal.models import Event


class EventModelRemarkForm(forms.ModelForm):
    class Meta:
        model  = Event
        exclude = ['form']