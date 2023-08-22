from django import forms
from selfappraisal.models import SelfAppraisalForm, Event, Course, KnowledgeResources

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


class SelfAppraisalKnowledgeModelFormMain(forms.ModelForm):
    class Meta:
        model = SelfAppraisalForm

        fields = [
            'projects_guided',
            'students_guided'
        ]

class SelfAppraisalStudentsGuidedFormMain(forms.ModelForm):
    class Meta:
        model = SelfAppraisalForm

        fields = [
            'learning_methodology',
            'modifications_in_teaching',
            'beyond_syllabus'
        ]

class EventModelForm(forms.ModelForm):
    class Meta:
        model  = Event
        exclude = ['form']

class CourseModelForm(forms.ModelForm):
    class Meta:
        model  = Course
        exclude = ['form']

class KnowledgeResourcesModelForm(forms.ModelForm):
    class Meta:
        model  = KnowledgeResources
        exclude = ['form']