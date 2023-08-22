from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from selfappraisal.form import SelfAppraisalFormModelFormMain, EventModelForm
from selfappraisal.models import SelfAppraisalForm, Event
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

# TODO: @rishabh fix this 
def delete_event_view(request, pk, event_id):
    event = get_object_or_404(Event, id=event_id)
    if event.form.id == pk:
        event.delete()
    formdashboard_url = reverse("formdashboard", kwargs={"pk": pk})
    return HttpResponseRedirect(formdashboard_url)

def form_dashboard_view(request, pk):
    mainform_obj = SelfAppraisalForm.objects.get(pk=pk)
    events = Event.objects.filter(form=mainform_obj)
    # create fo
    return render(request, 'selfappraisal/form/form_dashboard.html', {'form': mainform_obj, 'events': events})