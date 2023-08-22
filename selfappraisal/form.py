from django import forms
from selfappraisal.models import SelfAppraisalForm, Event, Course, KnowledgeResources, ResearchProject, Publication, ResearchGuidance

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

class SelfAppraisalActivitiesFormMain(forms.ModelForm):
    class Meta:
        model = SelfAppraisalForm

        fields = [
            'students_extra_curricular',
            'departmental_activities',
            'institute_activities',
            'invited_lectures',
            'articles_monographs',
        ]

class SelfAppraisalEndFormMain(forms.ModelForm):
    class Meta:
        model = SelfAppraisalForm

        fields = [
            'member_of_professional_bodies',
            'any_other_information',
            'list_of_enclosures',
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

class ResearchProjectModelForm(forms.ModelForm):
    class Meta:
        model  = ResearchProject
        exclude = ['form']

class PublicationModelForm(forms.ModelForm):
    class Meta:
        model  = Publication
        exclude = ['form']

class ResearchGuidanceModelForm(forms.ModelForm):
    class Meta:
        model  = ResearchGuidance
        exclude = ['form']
