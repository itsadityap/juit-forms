from django.shortcuts import render
from selfappraisal.models import SelfAppraisalForm, Event, Course, KnowledgeResources, ResearchProject, Publication, ResearchGuidance, EvaluationDuties
# Create your views here.

from django.views.generic import UpdateView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from formreview.form import EventModelRemarkForm, SelfAppraisalFormCourseRemarkForm, SelfAppraisalKnowledge, SelfAppraisalFormStudents

from django.http import Http404

def home(request):
    draft_forms = SelfAppraisalForm.objects.filter(department=request.user.department).filter(
        self_approval=True, hod_approval=False, dean_approval=False, vc_approval=False
    )
    return render(request, 'formreview/form_list.html', context={'draft_forms': draft_forms})

def form_review(request, pk):
    mainform_obj = SelfAppraisalForm.objects.get(id=pk)

    events = Event.objects.filter(form=mainform_obj)
    oddsemcourses = Course.objects.filter(form=mainform_obj, course_type=1)
    evensemcourses = Course.objects.filter(form=mainform_obj, course_type=2)

    knowledge_resources = KnowledgeResources.objects.filter(form=mainform_obj)
    research_projects = ResearchProject.objects.filter(form=mainform_obj)
    publications_papers = Publication.objects.filter(form=mainform_obj, publication_choice=1)
    publications_books = Publication.objects.filter(form=mainform_obj, publication_choice=2)
    research_guidances = ResearchGuidance.objects.filter(form=mainform_obj)

    try:
        evaluation_duties = EvaluationDuties.objects.get(form=mainform_obj)
    except EvaluationDuties.DoesNotExist:
        evaluation_duties = None


    return render(request, 'formreview/form_review.html', 
                    {
                        'form': mainform_obj, 
                        'events': events, 
                        'oddsemcourses': oddsemcourses, 
                        'evensemcourses': evensemcourses,
                        'knowledge_resources': knowledge_resources,
                        'research_projects': research_projects,
                        'publication_papers': publications_papers,
                        'publication_books': publications_books,
                        'research_guidances': research_guidances,
                        'evaluation_duties': evaluation_duties
                    }
                )

class AddEventRemarkView(UpdateView):
    model = Event
    form_class = EventModelRemarkForm
    template_name = 'formreview/add_event_remark.html'
    success_message = "Remark Added Successfully"
    
    def get_object(self, queryset=None):
        event_id = self.kwargs.get('event_id')
        event = get_object_or_404(Event, id=event_id)

        if event.form.pk != self.kwargs['pk']:
            raise Http404("No matches the given query.")
        
        return event
    
    def get_success_url(self):
        return reverse_lazy("formreview:form_review", kwargs={'pk': self.kwargs['pk']})


class SelfAppraisalCourseRemarkExtensionView(UpdateView):
    model = SelfAppraisalForm
    form_class = SelfAppraisalFormCourseRemarkForm
    template_name = 'formreview/create_course_remark_extension.html'
    success_message = "Form updated successfully"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("formreview:form_review", kwargs={'pk': self.kwargs['pk']})
    
class SelfAppraisalStudentsRemarkExtensionView(UpdateView):
    model = SelfAppraisalForm
    form_class = SelfAppraisalFormStudents
    template_name = 'formreview/create_student_remark_extension.html'
    success_message = "Form updated successfully"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("formreview:form_review", kwargs={'pk': self.kwargs['pk']})

class SelfAppraisalKnowledgeRemark(UpdateView):
    model = SelfAppraisalForm
    form_class = SelfAppraisalKnowledge
    template_name = 'formreview/create_knowledge_remark_extension.html'
    success_message = "Form updated successfully"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("formreview:form_review", kwargs={'pk': self.kwargs['pk']})