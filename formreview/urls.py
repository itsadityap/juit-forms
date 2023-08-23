from django.urls import path
from formreview.views import home, form_review, AddEventRemarkView

app_name = 'formreview'

urlpatterns = [
    path('home', home, name='home'),
    path('form_review/<int:pk>', form_review, name='form_review'),
    path('form_review/<int:pk>/event/<int:event_id>/addremarks', AddEventRemarkView.as_view(), name='add-event-remark'),
]