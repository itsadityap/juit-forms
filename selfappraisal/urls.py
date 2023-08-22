from django.urls import path
from selfappraisal import views

urlpatterns = [
    path('', views.home_view, name='home'),
    # path('form/', views.FormView.as_view(), name='form'),
    # Main Form CRUD
    path('form/', views.SelfAppraisalFormCreateView.as_view(), name='createmainform'),
    path('form/<int:pk>/update', views.SelfAppraisalFormUpdateView.as_view(), name='updatemainform'),
    path('form/<int:pk>/', views.form_dashboard_view, name='formdashboard'),


    
]
