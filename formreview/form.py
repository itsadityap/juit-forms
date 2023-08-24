from django import forms
from selfappraisal.models import Event, SelfAppraisalForm


class EventModelRemarkForm(forms.ModelForm):
    class Meta:
        model  = Event
        exclude = ['form']

class SelfAppraisalFormCourseRemarkForm(forms.ModelForm):
    class Meta:
        model = SelfAppraisalForm
        fields = [
            'courses_remarks_odd',
            'courses_remarks_even'
        ]

class SelfAppraisalKnowledge(forms.ModelForm):
    class Meta:
        model = SelfAppraisalForm

        fields = [
            'learning_methodology',
            'modifications_in_teaching',
            'beyond_syllabus',
            'knowledge_resources_remarks'
        ]

class SelfAppraisalFormStudents(forms.ModelForm):
    class Meta:
        model = SelfAppraisalForm
        fields = [
            'projects_guided_remarks',
            'students_guided_remarks'
        ]