from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'html/form-layout-1.html', {})
    # return render(request, 'form/base.html', {})