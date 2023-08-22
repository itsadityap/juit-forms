from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, UpdateView
from selfappraisal.form import SelfAppraisalFormModelFormMain, EventModelForm
from selfappraisal.models import SelfAppraisalForm, Event
from django.urls import reverse_lazy

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
        return reverse_lazy("home", kwargs={'pk': self.object.pk})


class EventCreateView(CreateView):
    model = Event
    form_class = EventModelForm
    template_name = 'selfappraisal/form/form.html'
    success_message = "Form updated successfully"

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # Use self.object to access the updated form instance
        return reverse_lazy("home", kwargs={'pk': self.object.pk})


def form_dashboard_view(request, pk):
    mainform_obj = SelfAppraisalForm.objects.get(pk=pk)

    # create fo
    return render(request, 'selfappraisal/form/form_dashboard.html', {'form': mainform_obj})