from django.urls import path
from selfappraisal import views

urlpatterns = [
    path('', views.home_view, name='home'),

    # Main Form 
    path('form/', views.SelfAppraisalFormCreateView.as_view(), name='createmainform'),
    path('form/<int:pk>/update', views.SelfAppraisalFormUpdateView.as_view(), name='updatemainform'),
    path('form/<int:pk>/', views.form_dashboard_view, name='formdashboard'),
    path('form/<int:pk>/knowledge-extension', views.SelfAppraisalKnowledgeExtensionView.as_view(), name='knowledge-extension'),
    path('form/<int:pk>/guided-extension', views.SelfAppraisalGuidedExtensionView.as_view(), name='guided-extension'),
    path('form/<int:pk>/activities', views.SelfAppraisalActivitiesView.as_view(), name='activity-extension'),
    path('form/<int:pk>/end', views.SelfAppraisalEndView.as_view(), name='end-extension'),

    # Event CRUD
    path('form/<int:pk>/event/create/', views.EventCreateView.as_view(), name="createevent"),
    path('form/<int:pk>/event/<int:event_id>/update/', views.EventUpdateView.as_view(), name="update-event"),
    path('form/<int:pk>/event/<int:event_id>/delete/', views.delete_event_view, name="delete-event"),

    # Course CRUD
    path('form/<int:pk>/course/create/', views.CourseCreateView.as_view(), name="create-course"),

    # Knowledge Resources CRUD
    path('form/<int:pk>/knowledge-resources/create/', views.KnowledgeResourcesCreateView.as_view(), name="create-knowledge-resources"),

    # Research Project CRUD
    path('form/<int:pk>/research-project/create/', views.ResearchProjectCreateView.as_view(), name="create-research-project"),

    # Publication CRUD
    path('form/<int:pk>/publication/create/', views.PublicationCreateView.as_view(), name="create-publication"),

    # Research Guidance CRUD
    path('form/<int:pk>/research-guidance/create/', views.ResearchGuidanceCreateView.as_view(), name="create-research-guidance"),
]
