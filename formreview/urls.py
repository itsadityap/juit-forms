from django.urls import path
from formreview.views import home, form_review, AddEventRemarkView,SelfAppraisalCourseRemarkExtensionView,SelfAppraisalKnowledgeRemark,SelfAppraisalStudentsRemarkExtensionView

app_name = 'formreview'

urlpatterns = [
    path('home', home, name='home'),
    path('form_review/<int:pk>', form_review, name='form_review'),
    path('form_review/<int:pk>/event/<int:event_id>/addremarks', AddEventRemarkView.as_view(), name='add-event-remark'),
    path('form_review/<int:pk>/course/addremarks', SelfAppraisalCourseRemarkExtensionView.as_view(), name='add-course-remark'),
    path('form_review/<int:pk>/knowledge/addremarks', SelfAppraisalKnowledgeRemark.as_view(), name='add-knowledge-remark'),
    path('form_review/<int:pk>/students/addremarks', SelfAppraisalStudentsRemarkExtensionView.as_view(), name='add-students-remark'),
]