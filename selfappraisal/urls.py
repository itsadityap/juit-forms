from django.urls import path
from selfappraisal import views

urlpatterns = [
    path('', views.home_view, name='home'),
    # path('form/', views.FormView.as_view(), name='form'),
    # Main Form CRUD
    path('form/', views.SelfAppraisalFormCreateView.as_view(), name='createmainform'),
    path('form/<int:pk>/update', views.SelfAppraisalFormUpdateView.as_view(), name='updatemainform'),
    path('form/<int:pk>/', views.form_dashboard_view, name='formdashboard'),
    path('form/<int:pk>/event/create/', views.EventCreateView.as_view(), name="createevent"),
    path('form/<int:pk>/event/<int:event_id>/update/', views.EventUpdateView.as_view(), name="update-event"),
    path('form/<int:pk>/event/<int:event_id>/delete/', views.delete_event_view, name="delete-event"),

]
