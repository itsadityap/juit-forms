from django.urls import path
from selfappraisal import views

urlpatterns = [
    path('', views.home_view, name='home'),
    # path('form/', views.FormView.as_view(), name='form'),
    path('form/', views.SelfAppraisalFormCreateView.as_view(), name='createform'),
    path('form/2', views.EventFormCreateView.as_view(), name='createevent')
]
