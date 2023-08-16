from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from selfappraisal.models import CustomUser, SelfAppraisalForm, Event, Course, KnowledgeResources, EvaluationDuties,Publication


admin.site.register(CustomUser, UserAdmin)


class EventInline(admin.TabularInline):
    model = Event
    fields = (
        'title',
        'start_date',
        'end_date',
        'sponsoring_agency',
        'organization',
        'place_held',
        'attended_organized',
        'remarks',
    )
    extra = 1

class CourseInline(admin.TabularInline):
    model = Course
    fields = (
        'course_code',
        'course_title',
        'contact_hours_per_week',
        'total_hours_scheduled',
        'total_hours_engaged',
        'self_assessed_api_score',
        'remarks',
    )
    extra = 1

class KnowledgeResourcesInline(admin.TabularInline):
    model = KnowledgeResources
    fields = (
        "course_code",
        'resources_consulted', 
        'resources_prescribed', 
        'additional_resources_provided', 
        'self_assessed_api_score', 
        'remarks', 
    )
    extra = 1

class EvaluationDutiesInline(admin.TabularInline):

    model = EvaluationDuties
    fields = (
        'q_papers_set',
        'ab_evaluated',
        'students_examined',
        'invigilation_duties',
        'api_score',
        'hod_remarks',
    )
    extra = 1

class PublicationInline(admin.TabularInline):
    model = Publication
    fields = (
        'author_names',
        'title_reference',
        'publication_type',
        'api_score',
        'remarks'
    )
    extra = 1

@admin.register(SelfAppraisalForm)
class SelfAppraisalFormAdmin(admin.ModelAdmin):
    inlines = [EventInline, CourseInline,KnowledgeResourcesInline, EvaluationDutiesInline, PublicationInline]




admin.site.register(Event)
admin.site.register(Course)