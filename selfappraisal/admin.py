from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from selfappraisal.models import CustomUser, SelfAppraisalForm, Event, Course, KnowledgeResources, EvaluationDuties,Publication,ResearchProject, ResearchGuidance

class CustomUserAdmin(UserAdmin):
    # Add custom fields to the fieldsets
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Departmenatal info', {'fields': ('department', 'user_type')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),        
    )


admin.site.register(CustomUser, CustomUserAdmin)


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
    extra = 0

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
    extra = 0

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
    extra = 0

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
    extra = 0

class PublicationInline(admin.TabularInline):
    model = Publication
    fields = (
        'author_names',
        'title_reference',
        'publication_type',
        'api_score',
        'remarks'
    )
    extra = 0

class ResearchProjectInline(admin.TabularInline):
    model = ResearchProject
    fields = (
        'title',
        'sponsoring_agency',
        'sanction_date',
        'duration',
        'status',
        'amount_sanctioned',
        'chief_investigator',
        'api_score',
        'remarks'
    )
    extra = 0

class ResearchGuidanceInline(admin.TabularInline):
    model = ResearchGuidance
    fields = (
        'enrollment_number', 
        'name_of_student', 
        'title_of_thesis', 
        'names_of_joint_supervisors',
        'level',
        'status', 
        'api_score', 
        'remarks'
    )
    extra = 0


@admin.register(SelfAppraisalForm)
class SelfAppraisalFormAdmin(admin.ModelAdmin):
    inlines = [EventInline, CourseInline,KnowledgeResourcesInline, EvaluationDutiesInline, PublicationInline,ResearchProjectInline,ResearchGuidanceInline]

    fieldsets = (
        ('Personal Details', {'fields': ('name', 'department', 'qualifications', 'present_designation', 'date_of_joining', 'first_designation', 'present_pay_scale_and_pay', 'areas_of_specialization', 'additional_qualifications', 'pursuing_higher_studies')}),
        ('Teaching, Learning and Evaluation Activities', {'fields': ('learning_methodology', 'modifications_in_teaching', 'beyond_syllabus')}),
        ('Project Guidance at UG level', {'fields': ('projects_guided', 'students_guided')}),
        ('Contribution/ Participation', {'fields': ('students_extra_curricular', 'departmental_activities', 'institute_activities', 'invited_lectures')}),
        ('Exta Info', {'fields': ('member_of_professional_bodies', 'any_other_information', 'list_of_enclosures')}),
        ('Approvals', {'fields': ('self_approval', 'hod_approval', 'hod_remarks', 'dean_approval', 'dean_remarks', 'vc_approval', 'vc_remarks')}),
    )




admin.site.register(Event)
admin.site.register(Course)
admin.site.register(EvaluationDuties)