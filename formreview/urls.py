from django.urls import path
from formreview.views import home, form_review

app_name = 'formreview'

urlpatterns = [
    path('home', home, name='home'),
    path('form_review/<int:pk>', form_review, name='form_review'),
]