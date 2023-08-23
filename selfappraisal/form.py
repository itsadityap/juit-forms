from django import forms
from selfappraisal.models import EvaluationDuties,SelfAppraisalForm, Event, Course, KnowledgeResources, ResearchProject, Publication, ResearchGuidance

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

class EvaluationDutiesForm(forms.ModelForm):
    class Meta:
        model = EvaluationDuties
        fields = (
            'q_papers_set', 
            'ab_evaluated', 
            'students_examined', 
            'invigilation_duties',
        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        json_fields = ['q_papers_set', 'ab_evaluated', 'students_examined', 'invigilation_duties']
        for field_name in json_fields:
            initial_data = getattr(self.instance, field_name, {})
            for key in initial_data:
                for index, value in enumerate(initial_data[key]):
                    field_key = f'{field_name}_{key}_{index}'
                    print(field_key)
                    self.fields[field_key] = forms.IntegerField(initial=value)
                    self.fields[field_key].label = f'{key.capitalize()} {index + 1}'
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        
        json_fields = ['q_papers_set', 'ab_evaluated', 'students_examined', 'invigilation_duties']
        for field_name in json_fields:
            json_data = self.cleaned_data[field_name]
            for key in json_data:
                json_data[key] = [self.cleaned_data[f'{field_name}_{key}_{index}'] for index in range(len(json_data[key]))]
            setattr(instance, field_name, json_data)
        
        if commit:
            instance.save()
        return instance
