from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from selfappraisal.form import EvaluationDutiesForm,SelfAppraisalEndFormMain,SelfAppraisalFormModelFormMain,SelfAppraisalActivitiesFormMain, EventModelForm, CourseModelForm, KnowledgeResourcesModelForm, SelfAppraisalKnowledgeModelFormMain, SelfAppraisalKnowledgeModelFormMain, ResearchProjectModelForm, PublicationModelForm, ResearchGuidanceModelForm
from selfappraisal.models import EvaluationDuties,SelfAppraisalForm, Event, Course, KnowledgeResources, ResearchProject, Publication, ResearchGuidance
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseRedirect

# Create your views here.
def home_view(request):
    return render(request, 'selfappraisal/dashboard/dashboard.html', {})

class SelfAppraisalFormCreateView(CreateView):
    model = SelfAppraisalForm
    form_class = SelfAppraisalFormModelFormMain
    template_name = 'selfappraisal/form/form.html'
    success_message = "Form submitted successfully"

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # Use self.object to access the newly created form instance
        return reverse_lazy("formdashboard", kwargs={'pk': self.object.pk})
    
class SelfAppraisalFormUpdateView(UpdateView):
    model = SelfAppraisalForm
    form_class = SelfAppraisalFormModelFormMain
    template_name = 'selfappraisal/form/form.html'
    success_message = "Form updated successfully"

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # Use self.object to access the updated form instance
        return reverse_lazy("formdashboard", kwargs={'pk': self.object.pk})
    
class SelfAppraisalKnowledgeExtensionView(UpdateView):
    model = SelfAppraisalForm
    form_class = SelfAppraisalKnowledgeModelFormMain
    template_name = 'selfappraisal/form/create_knowledge_extension.html'
    success_message = "Form updated successfully"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("formdashboard", kwargs={'pk': self.object.pk})

class SelfAppraisalGuidedExtensionView(UpdateView):
    model = SelfAppraisalForm
    form_class = SelfAppraisalKnowledgeModelFormMain
    template_name = 'selfappraisal/form/create_students_guided.html'
    success_message = "Form updated successfully"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("formdashboard", kwargs={'pk': self.object.pk})

class SelfAppraisalActivitiesView(UpdateView):
    model = SelfAppraisalForm
    form_class = SelfAppraisalActivitiesFormMain
    template_name = 'selfappraisal/form/create_activities.html'
    success_message = "Form updated successfully"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("formdashboard", kwargs={'pk': self.object.pk})
    
class SelfAppraisalEndView(UpdateView):
    model = SelfAppraisalForm
    form_class = SelfAppraisalEndFormMain
    template_name = 'selfappraisal/form/create_end.html'
    success_message = "Form updated successfully"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("formdashboard", kwargs={'pk': self.object.pk})

class EventCreateView(CreateView):
    model = Event
    form_class = EventModelForm
    template_name = 'selfappraisal/form/create_event.html'
    success_message = "Hello" # TODO: ADD

    def form_valid(self, form):
        # TODO: ADD PROTECTION
        form.instance.form = SelfAppraisalForm.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        # Use self.object to access the updated form instance
        return reverse_lazy("formdashboard", kwargs={'pk': self.kwargs['pk']})

class EventUpdateView(UpdateView):
    model = Event
    form_class = EventModelForm
    template_name = 'selfappraisal/form/create_event.html'
    success_message = "Hello" # TODO: ADD
    
    def get_object(self, queryset=None):
        event_id = self.kwargs.get('event_id')
        event = get_object_or_404(Event, id=event_id)

        if event.form.id != self.kwargs['pk']:
            raise Http404("No matches the given query.")

        return event
    
    def get_success_url(self):
        # Use self.object to access the updated form instance
        return reverse_lazy("formdashboard", kwargs={'pk': self.kwargs['pk']})


# TODO: MAKE UPDATE DELETE
class CourseCreateView(CreateView):
    model = Course
    form_class = CourseModelForm
    template_name = 'selfappraisal/form/create_course.html'
    success_message = "Hello" # TODO: ADD

    def form_valid(self, form):
        # TODO: ADD PROTECTION
        form.instance.form = SelfAppraisalForm.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        # Use self.object to access the updated form instance
        return reverse_lazy("formdashboard", kwargs={'pk': self.kwargs['pk']})

class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseModelForm
    template_name = 'selfappraisal/form/create_course.html'
    success_message = "Hello" # TODO: ADD
    
    def get_object(self, queryset=None):
        event_id = self.kwargs.get('event_id')
        event = get_object_or_404(Event, id=event_id)

        if event.form.id != self.kwargs['pk']:
            raise Http404("No matches the given query.")

        return event
    
    def get_success_url(self):
        # Use self.object to access the updated form instance
        return reverse_lazy("formdashboard", kwargs={'pk': self.kwargs['pk']})

class KnowledgeResourcesCreateView(CreateView):
    model = KnowledgeResources
    form_class = KnowledgeResourcesModelForm
    template_name = 'selfappraisal/form/create_resource.html'
    success_message = "Hello" # TODO: ADD

    def form_valid(self, form):
        # TODO: ADD PROTECTION
        form.instance.form = SelfAppraisalForm.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        # Use self.object to access the updated form instance
        return reverse_lazy("formdashboard", kwargs={'pk': self.kwargs['pk']})

# TODO: @rishabh fix this 
def delete_event_view(request, pk, event_id):
    event = get_object_or_404(Event, id=event_id)
    if event.form.id == pk:
        event.delete()
    formdashboard_url = reverse("formdashboard", kwargs={"pk": pk})
    return HttpResponseRedirect(formdashboard_url)

class ResearchProjectCreateView(CreateView):
    model = ResearchProject
    form_class = ResearchProjectModelForm
    template_name = 'selfappraisal/form/create_research_projects.html'
    success_message = "Hello" # TODO: ADD

    def form_valid(self, form):
        form.instance.form = SelfAppraisalForm.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        # Use self.object to access the updated form instance
        return reverse_lazy("formdashboard", kwargs={'pk': self.kwargs['pk']})
    

class PublicationCreateView(CreateView):
    model = Publication
    form_class = PublicationModelForm
    template_name = 'selfappraisal/form/create_books_publications.html'
    success_message = "Hello" # TODO: ADD

    def form_valid(self, form):
        form.instance.form = SelfAppraisalForm.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        # Use self.object to access the updated form instance
        return reverse_lazy("formdashboard", kwargs={'pk': self.kwargs['pk']})


class ResearchGuidanceCreateView(CreateView):
    model = ResearchGuidance
    form_class = ResearchGuidanceModelForm
    template_name = 'selfappraisal/form/create_research_guidance.html'
    success_message = "Hello" # TODO: ADD

    def form_valid(self, form):
        form.instance.form = SelfAppraisalForm.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        # Use self.object to access the updated form instance
        return reverse_lazy("formdashboard", kwargs={'pk': self.kwargs['pk']})

class EvolutionOfCoursesCreateView(CreateView):
    model = EvaluationDuties
    form_class = EvaluationDutiesForm
    template_name = 'selfappraisal/form/create_evolution_duties.html'
    success_message = "Hello" # TODO: ADD

    def form_valid(self, form):
        form.instance.form = SelfAppraisalForm.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        # Use self.object to access the updated form instance
        return reverse_lazy("formdashboard", kwargs={'pk': self.kwargs['pk']})

class EvolutionOfCoursesUpdateView(UpdateView):
    model = EvaluationDuties
    form_class = EvaluationDutiesForm
    template_name = 'selfappraisal/form/create_evolution_duties.html'
    success_message = "Hello" # TODO: ADD

    def get_object(self, queryset=None):
        eval_obj = self.kwargs.get('evolution_of_courses_id')
        event = get_object_or_404(EvaluationDuties, id=eval_obj)

        if event.form.id != self.kwargs['pk']:
            raise Http404("No matches the given query.")

        return event

    def get_success_url(self):
        # Use self.object to access the updated form instance
        return reverse_lazy("formdashboard", kwargs={'pk': self.kwargs['pk']})
    

def form_dashboard_view(request, pk):
    mainform_obj = SelfAppraisalForm.objects.get(pk=pk)
    events = Event.objects.filter(form=mainform_obj)
    oddsemcourses = Course.objects.filter(form=mainform_obj, course_type=1)
    evensemcourses = Course.objects.filter(form=mainform_obj, course_type=2)

    knowledge_resources = KnowledgeResources.objects.filter(form=mainform_obj)
    # create fo
    research_projects = ResearchProject.objects.filter(form=mainform_obj)
    publications_papers = Publication.objects.filter(form=mainform_obj, publication_choice=1)
    publications_books = Publication.objects.filter(form=mainform_obj, publication_choice=2)
    research_guidances = ResearchGuidance.objects.filter(form=mainform_obj)

    try:
        evaluation_duties = EvaluationDuties.objects.get(form=mainform_obj)
    except EvaluationDuties.DoesNotExist:
        evaluation_duties = None


    
    return render(request, 'selfappraisal/form/form_dashboard.html', 
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