from django import forms
from selfappraisal.models import SelfAppraisalForm, Event

class SelfAppraisalFormModelFormMain(forms.ModelForm):
    class Meta:
        model = SelfAppraisalForm

        fields = [
            'department',
            'qualifications',
            'present_designation',
            'date_of_joining',
            'first_designation',
            'present_pay_scale_and_pay',
            'areas_of_specialization',
            'additional_qualifications',
            'pursuing_higher_studies',
        ]

class EventModelForm(forms.ModelForm):
    class Meta:
        model  = Event
        exclude = ['form']