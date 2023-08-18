from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from selfappraisal.form import SelfAppraisalFormModelForm, EventModelForm
from selfappraisal.models import SelfAppraisalForm, Event
from django.urls import reverse_lazy

# Create your views here.
def home_view(request):
    return render(request, 'selfappraisal/dashboard/dashboard.html', {})

# class FormView(View):
#     def get(self, request):
#         return render(request, 'selfappraisal/form/form.html', {})

class SelfAppraisalFormCreateView(CreateView):
    model = SelfAppraisalForm
    form_class = SelfAppraisalFormModelForm
    template_name = 'selfappraisal/form/form.html'
    success_url = reverse_lazy("home")
    success_message = "Form submitted successfully"

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)
    

class EventFormCreateView(CreateView):
    model = Event
    form_class = EventModelForm
    template_name = 'selfappraisal/form/event_form.html'
    success_url = reverse_lazy("home")
    success_message = "Event added successfully"

    def form_valid(self, form):
        form.instance.form = SelfAppraisalForm.objects.get(name=self.request.user)
        return super().form_valid(form)