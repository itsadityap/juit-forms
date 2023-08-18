from django import forms
from selfappraisal.models import SelfAppraisalForm, Event

class SelfAppraisalFormModelForm(forms.ModelForm):
    class Meta:
        model = SelfAppraisalForm

        exclude = ['name', 'self_approval', 'hod_approval', 'hod_remarks', 'dean_approval', 'dean_remarks', 'vc_approval', 'vc_remarks']
        # widgets = {'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'})}

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.fields['title'].widget.attrs['class'] = 'form-control'

class EventModelForm(forms.ModelForm):
    class Meta:
        model  = Event
        exclude = ['form']