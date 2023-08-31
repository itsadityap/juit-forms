from django.shortcuts import render
from selfappraisal.models import SelfAppraisalForm, Event, Course, KnowledgeResources, ResearchProject, Publication, ResearchGuidance, EvaluationDuties
# Create your views here.
from django.http import Http404, HttpResponseRedirect

from django.views.generic import UpdateView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse

from formreview.form import EventModelRemarkForm

from django.http import Http404

def home(request):
    draft_forms = None

    if request.user.user_type == 1:
        draft_forms = SelfAppraisalForm.objects.filter(department=request.user.department).filter(
            self_approval=True, hod_approval=False, dean_approval=False, vc_approval=False
        )
    elif request.user.user_type == 2:
        draft_forms = SelfAppraisalForm.objects.filter(
            self_approval=True, hod_approval=True, dean_approval=False, vc_approval=False
        )
    elif request.user.user_type == 3:
        draft_forms = SelfAppraisalForm.objects.filter(
            self_approval=True, hod_approval=True, dean_approval=True, vc_approval=False
        )

    return render(request, 'formreview/form_list.html', context={'draft_forms': draft_forms})

def form_review(request, pk):
    mainform_obj = SelfAppraisalForm.objects.get(id=pk)

    if request.method == 'POST':
        sumitcheck = request.POST.get('submitform')
        if sumitcheck:
            if request.user.user_type == 1:
                mainform_obj.hod_approval = True
            elif request.user.user_type == 2:
                mainform_obj.dean_approval = True
            elif request.user.user_type == 3:
                mainform_obj.vc_approval = True
                
            mainform_obj.save()
            return HttpResponseRedirect(reverse('home'))

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
    fields = [
        'courses_remarks_odd',
        'courses_remarks_even'
    ]
    template_name = 'formreview/create_course_remark_extension.html'
    success_message = "Form updated successfully"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("formreview:form_review", kwargs={'pk': self.kwargs['pk']})
    
class SelfAppraisalStudentsRemarkExtensionView(UpdateView):
    model = SelfAppraisalForm
    fields = [
        'projects_guided_remarks',
        'students_guided_remarks'
    ]
    template_name = 'formreview/create_student_remark_extension.html'
    success_message = "Form updated successfully"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("formreview:form_review", kwargs={'pk': self.kwargs['pk']})

class SelfAppraisalKnowledgeRemark(UpdateView):
    model = SelfAppraisalForm
    fields = [
        'learning_methodology',
        'modifications_in_teaching',
        'beyond_syllabus',
        'knowledge_resources_remarks'
    ]
    template_name = 'formreview/create_knowledge_remark_extension.html'
    success_message = "Form updated successfully"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("formreview:form_review", kwargs={'pk': self.kwargs['pk']})
    
class SelfAppraisalExaminationDutiesRemark(UpdateView):
    model = SelfAppraisalForm
    fields = ['examination_duties_remarks']
    template_name = 'formreview/create_evaluation_duties_extension.html'
    success_message = "Form updated successfully"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("formreview:form_review", kwargs={'pk': self.kwargs['pk']})

#Research Papers Published/ Presented:
class SelfAppraisalResearchPaperRemark(UpdateView):
    model = SelfAppraisalForm
    fields = ['research_paper_remarks']
    template_name = 'formreview/create_extension_form.html'
    success_message = "Form updated successfully"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("formreview:form_review", kwargs={'pk': self.kwargs['pk']})
    
class SelfAppraisalBooksRemark(UpdateView):
    model = SelfAppraisalForm
    fields = ['books_remarks']
    template_name = 'formreview/create_extension_form.html'
    success_message = "Form updated successfully"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("formreview:form_review", kwargs={'pk': self.kwargs['pk']})
    
class SelfAppraisalResearchProjectsRemark(UpdateView):
    model = SelfAppraisalForm
    fields = ['research_projects_remarks']
    template_name = 'formreview/create_extension_form.html'
    success_message = "Form updated successfully"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("formreview:form_review", kwargs={'pk': self.kwargs['pk']})

class SelfAppraisalResearchGuidanceRemark(UpdateView):
    model = SelfAppraisalForm
    fields = ['research_guidance_remarks']
    template_name = 'formreview/create_extension_form.html'
    success_message = "Form updated successfully"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("formreview:form_review", kwargs={'pk': self.kwargs['pk']})

class SelfAppraisalOverallRemarksemark(UpdateView):
    model = SelfAppraisalForm
    fields = ['overall_remarks']
    template_name = 'formreview/create_extension_form.html'
    success_message = "Form updated successfully"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("formreview:form_review", kwargs={'pk': self.kwargs['pk']})
