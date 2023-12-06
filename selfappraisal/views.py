from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from selfappraisal.form import EvaluationDutiesForm,SelfAppraisalEndFormMain,SelfAppraisalFormModelFormMain,SelfAppraisalActivitiesFormMain, EventModelForm, CourseModelForm, KnowledgeResourcesModelForm, SelfAppraisalKnowledgeModelFormMain, SelfAppraisalKnowledgeModelFormMain, ResearchProjectModelForm, PublicationModelForm, ResearchGuidanceModelForm
from selfappraisal.models import EvaluationDuties,SelfAppraisalForm, Event, Course, KnowledgeResources, ResearchProject, Publication, ResearchGuidance
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


class FormOwnershipCheckMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        
        # Check if the user has ownership over the form
        if form.instance.form.name != self.request.user:
            raise PermissionDenied("You do not have permission to update this form.")

        return form
    
class FormOwnershipCheckOnCreateMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        
        self.parent_form =  get_object_or_404(SelfAppraisalForm, pk=self.kwargs['pk'])

        # Check if the user has ownership over the form
        if self.parent_form.name != self.request.user:
            raise PermissionDenied("You do not have permission to update this form.")

        return form
    
class FormOwnershipTestExtensionMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        
        # Check if the user has ownership over the form
        if form.instance.name != self.request.user:
            raise PermissionDenied("You do not have permission to update this form.")

        return form

def check_model_ownership(request, model_obj):
    if request.user == model_obj.form.name:
        return True
    else:
        return False


class SelfAppraisalFormCreateView(LoginRequiredMixin, CreateView):
    model = SelfAppraisalForm
    form_class = SelfAppraisalFormModelFormMain
    template_name = 'selfappraisal/form/form.html'
    success_message = "Form submitted successfully"

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("formdashboard", kwargs={'pk': self.object.pk})
    
class SelfAppraisalFormUpdateView(LoginRequiredMixin,FormOwnershipTestExtensionMixin, UpdateView):
    model = SelfAppraisalForm
    form_class = SelfAppraisalFormModelFormMain
    template_name = 'selfappraisal/form/form.html'
    success_message = "Form updated successfully"
    
    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("formdashboard", kwargs={'pk': self.object.pk})
    
class SelfAppraisalKnowledgeExtensionView(LoginRequiredMixin,FormOwnershipTestExtensionMixin,UpdateView):
    model = SelfAppraisalForm
    form_class = SelfAppraisalKnowledgeModelFormMain
    template_name = 'selfappraisal/form/create_knowledge_extension.html'
    success_message = "Form updated successfully"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("formdashboard", kwargs={'pk': self.object.pk})

class SelfAppraisalGuidedExtensionView(LoginRequiredMixin,FormOwnershipTestExtensionMixin,UpdateView):
    model = SelfAppraisalForm
    form_class = SelfAppraisalKnowledgeModelFormMain
    template_name = 'selfappraisal/form/create_students_guided.html'
    success_message = "Form updated successfully"

    
    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("formdashboard", kwargs={'pk': self.object.pk})

class SelfAppraisalActivitiesView(LoginRequiredMixin,FormOwnershipTestExtensionMixin, UpdateView):
    model = SelfAppraisalForm
    form_class = SelfAppraisalActivitiesFormMain
    template_name = 'selfappraisal/form/create_activities.html'
    success_message = "Form updated successfully"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("formdashboard", kwargs={'pk': self.object.pk})
    
class SelfAppraisalEndView(LoginRequiredMixin,FormOwnershipTestExtensionMixin,UpdateView):
    model = SelfAppraisalForm
    form_class = SelfAppraisalEndFormMain
    template_name = 'selfappraisal/form/create_end.html'
    success_message = "Form updated successfully"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("formdashboard", kwargs={'pk': self.object.pk})

class EventCreateView(LoginRequiredMixin,FormOwnershipCheckOnCreateMixin,CreateView):
    model = Event
    form_class = EventModelForm
    template_name = 'selfappraisal/form/create_event.html'
    success_message = "Event created successfully" 

    def form_valid(self, form):
        form.instance.form = self.parent_form
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("formdashboard", kwargs={'pk': self.kwargs['pk']})

class EventUpdateView(LoginRequiredMixin,FormOwnershipCheckMixin,UpdateView):
    model = Event
    form_class = EventModelForm
    template_name = 'selfappraisal/form/create_event.html'
    success_message = "Event updated successfully"
    
    def get_object(self, queryset=None):
        event_id = self.kwargs.get('event_id')
        event = get_object_or_404(Event, id=event_id)

        if event.form.id != self.kwargs['pk']:
            raise Http404("No matches the given query.")
        return event
    
    def get_success_url(self):
        return reverse_lazy("formdashboard", kwargs={'pk': self.kwargs['pk']})

@login_required
def delete_event_view(request, pk, event_id):
    event = get_object_or_404(Event, id=event_id)

    if not check_model_ownership(request, event):
        raise PermissionDenied("You do not have permission to perform this action.")

    if event.form.id == pk:
        event.delete()
    formdashboard_url = reverse("formdashboard", kwargs={"pk": pk})
    return HttpResponseRedirect(formdashboard_url)

class CourseCreateView(LoginRequiredMixin,FormOwnershipCheckOnCreateMixin,CreateView):
    model = Course
    form_class = CourseModelForm
    template_name = 'selfappraisal/form/create_course.html'
    success_message = "Course Created Successfully"

    def form_valid(self, form):
        form.instance.form = self.parent_form
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("formdashboard", kwargs={'pk': self.kwargs['pk']})

class CourseUpdateView(LoginRequiredMixin,FormOwnershipCheckMixin,UpdateView):
    model = Course
    form_class = CourseModelForm
    template_name = 'selfappraisal/form/create_course.html'
    success_message = "Course Updated Successfully"
    
    def get_object(self, queryset=None):
        course_id = self.kwargs.get('course_id')
        course = get_object_or_404(Course, id=course_id)

        if course.form.id != self.kwargs['pk']:
            raise Http404("No matches the given query.")
        return course
    
    def get_success_url(self):
        return reverse_lazy("formdashboard", kwargs={'pk': self.kwargs['pk']})

@login_required
def delete_course_view(request, pk, course_id):
    course = get_object_or_404(Course, id=course_id)

    if not check_model_ownership(request, course):
        raise PermissionDenied("You do not have permission to perform this action.")
    

    if course.form.id == pk:
        course.delete()
    formdashboard_url = reverse("formdashboard", kwargs={"pk": pk})
    return HttpResponseRedirect(formdashboard_url)

class KnowledgeResourcesCreateView(LoginRequiredMixin,FormOwnershipCheckOnCreateMixin,CreateView):
    model = KnowledgeResources
    form_class = KnowledgeResourcesModelForm
    template_name = 'selfappraisal/form/create_resource.html'
    success_message = "Knowledge Resources Created Successfully"

    def form_valid(self, form):
        form.instance.form = self.parent_form
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("formdashboard", kwargs={'pk': self.kwargs['pk']})

class KnowledgeResourcesUpdateView(LoginRequiredMixin,FormOwnershipCheckMixin,UpdateView):
    model = KnowledgeResources
    form_class = KnowledgeResourcesModelForm
    template_name = 'selfappraisal/form/create_resource.html'
    success_message = "Knowledge Resources Updated Successfully"
    
    def get_object(self, queryset=None):
        knowledge_resource_id = self.kwargs.get('knowledge_resource_id')
        knowledge_resource = get_object_or_404(KnowledgeResources, id=knowledge_resource_id)

        if knowledge_resource.form.id != self.kwargs['pk']:
            raise Http404("No matches the given query.")
        return knowledge_resource
    
    def get_success_url(self):
        return reverse_lazy("formdashboard", kwargs={'pk': self.kwargs['pk']})

@login_required
def delete_knowledge_resources_view(request, pk, knowledge_resource_id):
    knowledge_resource = get_object_or_404(KnowledgeResources, id=knowledge_resource_id)

    if not check_model_ownership(request, knowledge_resource):
        raise PermissionDenied("You do not have permission to perform this action.")

    if knowledge_resource.form.id == pk:
        knowledge_resource.delete()
    formdashboard_url = reverse("formdashboard", kwargs={"pk": pk})
    return HttpResponseRedirect(formdashboard_url)


class ResearchProjectCreateView(LoginRequiredMixin,FormOwnershipCheckOnCreateMixin,CreateView):
    model = ResearchProject
    form_class = ResearchProjectModelForm
    template_name = 'selfappraisal/form/create_research_projects.html'
    success_message = "Research Project Created successfully"

    def form_valid(self, form):
        form.instance.form = self.parent_form
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("formdashboard", kwargs={'pk': self.kwargs['pk']})

class ResearchProjectUpdateView(LoginRequiredMixin,FormOwnershipCheckMixin,UpdateView):
    model = ResearchProject
    form_class = ResearchProjectModelForm
    template_name = 'selfappraisal/form/create_research_projects.html'
    success_message = "Research Project Updated successfully"

    def get_object(self, queryset=None):
        research_project_id = self.kwargs.get('research_project_id')
        research_project = get_object_or_404(ResearchProject, id=research_project_id)

        if research_project.form.id != self.kwargs['pk']:
            raise Http404("No matches the given query.")
        return research_project

    def get_success_url(self):
        return reverse_lazy("formdashboard", kwargs={'pk': self.kwargs['pk']})
    
@login_required
def delete_research_project_view(request, pk, research_project_id):
    research_project = get_object_or_404(ResearchProject, id=research_project_id)

    if not check_model_ownership(request, research_project):
        raise PermissionDenied("You do not have permission to perform this action.")

    if research_project.form.id == pk:
        research_project.delete()
    formdashboard_url = reverse("formdashboard", kwargs={"pk": pk})
    return HttpResponseRedirect(formdashboard_url)


class PublicationCreateView(LoginRequiredMixin,FormOwnershipCheckOnCreateMixin,CreateView):
    model = Publication
    form_class = PublicationModelForm
    template_name = 'selfappraisal/form/create_books_publications.html'
    success_message = "Publication Created Succesfully" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs.get('pk')
        return context
    
    def form_valid(self, form):
        form.instance.form = self.parent_form
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("formdashboard", kwargs={'pk': self.kwargs['pk']})


import threading
from selfappraisal.background_utils import add_research_paper

@login_required
def publication_using_google_scholar(request, pk):

    if request.method == "POST":
        mainform_obj = SelfAppraisalForm.objects.get(pk=pk)

        author_id = request.POST.get("google_profile_id")
        
        threading.Thread(target=add_research_paper, args=(author_id, mainform_obj)).start()
        
    formdashboard_url = reverse("formdashboard", kwargs={"pk": pk})
    return HttpResponseRedirect(formdashboard_url)    

@login_required
def publication_using_juitpub(request, pk):

    if request.method == "POST":
        mainform_obj = SelfAppraisalForm.objects.get(pk=pk)

        author_id = request.POST.get("google_profile_id")
        
        threading.Thread(target=add_research_paper, args=(author_id, mainform_obj)).start()
        
    formdashboard_url = reverse("formdashboard", kwargs={"pk": pk})
    return HttpResponseRedirect(formdashboard_url)    

class PublicationUpdateView(LoginRequiredMixin,FormOwnershipCheckMixin,UpdateView):
    model = Publication
    form_class = PublicationModelForm
    template_name = 'selfappraisal/form/create_books_publications.html'
    success_message = "Publication Updated Succesfully" 

    def get_object(self, queryset=None):
        publication_id = self.kwargs.get('publication_id')
        publication = get_object_or_404(Publication, id=publication_id)

        if publication.form.id != self.kwargs['pk']:
            raise Http404("No matches the given query.")
        return publication

    def get_success_url(self):
        return reverse_lazy("formdashboard", kwargs={'pk': self.kwargs['pk']})

@login_required
def delete_publication_view(request, pk, publication_id):
    publication = get_object_or_404(Publication, id=publication_id)

    if not check_model_ownership(request, publication):
        raise PermissionDenied("You do not have permission to perform this action.")
    

    if publication.form.id == pk:
        publication.delete()
    formdashboard_url = reverse("formdashboard", kwargs={"pk": pk})
    return HttpResponseRedirect(formdashboard_url)


class ResearchGuidanceUpdateView(LoginRequiredMixin,FormOwnershipCheckMixin,UpdateView):
    model = ResearchGuidance
    form_class = ResearchGuidanceModelForm
    template_name = 'selfappraisal/form/create_research_guidance.html'
    success_message = "Research Guidance Updated successfully" 

    def get_object(self, queryset=None):
        research_guidance_id = self.kwargs.get('research_guidance_id')
        research_guidance = get_object_or_404(ResearchGuidance, id=research_guidance_id)

        if research_guidance.form.id != self.kwargs['pk']:
            raise Http404("No matches the given query.")
        return research_guidance

    def get_success_url(self):
        return reverse_lazy("formdashboard", kwargs={'pk': self.kwargs['pk']})


class ResearchGuidanceCreateView(LoginRequiredMixin, FormOwnershipCheckOnCreateMixin,CreateView):
    model = ResearchGuidance
    form_class = ResearchGuidanceModelForm
    template_name = 'selfappraisal/form/create_research_guidance.html'
    success_message = "Research Guidance created successfully" 

    def form_valid(self, form):
        form.instance.form = self.parent_form
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("formdashboard", kwargs={'pk': self.kwargs['pk']})

@login_required
def delete_research_guidance_view(request, pk, research_guidance_id):
    research_guidance = get_object_or_404(ResearchGuidance, id=research_guidance_id)

    if not check_model_ownership(request, research_guidance):
        raise PermissionDenied("You do not have permission to perform this action.")

    if research_guidance.form.id == pk:
        research_guidance.delete()
    formdashboard_url = reverse("formdashboard", kwargs={"pk": pk})
    return HttpResponseRedirect(formdashboard_url)

class EvolutionOfCoursesCreateView(LoginRequiredMixin,FormOwnershipCheckOnCreateMixin,CreateView):
    model = EvaluationDuties
    form_class = EvaluationDutiesForm
    template_name = 'selfappraisal/form/create_evolution_duties.html'
    success_message = "Evolution of Course created successfully"

    def form_valid(self, form):
        form.instance.form = self.parent_form
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("formdashboard", kwargs={'pk': self.kwargs['pk']})

class EvolutionOfCoursesUpdateView(LoginRequiredMixin,FormOwnershipCheckMixin,UpdateView):
    model = EvaluationDuties
    form_class = EvaluationDutiesForm
    template_name = 'selfappraisal/form/create_evolution_duties.html'
    success_message = "Evolution of Course updated successfully"

    def get_object(self, queryset=None):
        eval_obj = self.kwargs.get('evolution_of_courses_id')
        event = get_object_or_404(EvaluationDuties, id=eval_obj)

        if event.form.id != self.kwargs['pk']:
            raise Http404("No matches the given query.")

        return event

    def get_success_url(self):
        return reverse_lazy("formdashboard", kwargs={'pk': self.kwargs['pk']})
    

@login_required
def form_dashboard_view(request, pk):

    mainform_obj = SelfAppraisalForm.objects.get(pk=pk)

    # if mainform_obj.name != request.user:
    #     raise PermissionDenied("You do not have permission to view this form.")

    if request.method == 'POST':
        sumitcheck = request.POST.get('submitform')
        if sumitcheck:
            mainform_obj.self_approval = True
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


@login_required
def home_view(request):
    forms_drafted = SelfAppraisalForm.objects.filter(name=request.user,self_approval = False )
    forms_under_review = SelfAppraisalForm.objects.filter(name=request.user,self_approval = True, vc_approval = False)
    forms_approved = SelfAppraisalForm.objects.filter(name=request.user,vc_approval=True)
    return render(request, 'selfappraisal/dashboard/dashboard.html', {
        'forms_drafted':forms_drafted,
        'forms_under_review':forms_under_review,
        'forms_approved':forms_approved
        })

