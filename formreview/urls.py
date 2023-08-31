from django.urls import path
from formreview import views

app_name = 'formreview'

urlpatterns = [
    path('home', views.home, name='home'),
    path('form_review/<int:pk>', views.form_review, name='form_review'),
    path('form_review/<int:pk>/event/<int:event_id>/addremarks', views.AddEventRemarkView.as_view(), name='add-event-remark'),
    path('form_review/<int:pk>/course/addremarks', views.SelfAppraisalCourseRemarkExtensionView.as_view(), name='add-course-remark'),
    path('form_review/<int:pk>/knowledge/addremarks', views.SelfAppraisalKnowledgeRemark.as_view(), name='add-knowledge-remark'),
    path('form_review/<int:pk>/students/addremarks', views.SelfAppraisalStudentsRemarkExtensionView.as_view(), name='add-students-remark'),
    path('form_review/<int:pk>/duties/addremarks', views.SelfAppraisalExaminationDutiesRemark.as_view(), name='add-duties-remark'),
    
    path('form_review/<int:pk>/researchpaper/addremarks', views.SelfAppraisalResearchPaperRemark.as_view(), name='add-research-paper-remark'),
    path('form_review/<int:pk>/researchguidance/addremarks', views.SelfAppraisalResearchGuidanceRemark.as_view(), name='add-research-guidance-remark'),
    path('form_review/<int:pk>/books/addremarks', views.SelfAppraisalBooksRemark.as_view(), name='add-books-remark'),
    path('form_review/<int:pk>/researchprojects/addremarks', views.SelfAppraisalResearchProjectsRemark.as_view(), name='add-research-projects-remark'),
    path('form_review/<int:pk>/overallhod/addremarks', views.SelfAppraisalOverallRemarksemark.as_view(), name='add-overall-hod'),
]