from django.db import models
from django.conf import settings


from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    pass


# Create your models here.

class SelfAppraisalForm(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Name
    
    department = models.CharField(max_length=100, null=True)  # Department
    
    qualifications = models.CharField(max_length=100,null=True) # Qualifications

    present_designation = models.CharField(max_length=100,null=True) # Present Designation
    
    date_of_joining = models.DateField(null=True) # University Joining Date

    first_designation = models.CharField(max_length=100,null=True) # First Designation

    present_pay_scale_and_pay = models.CharField(max_length=100,null=True) # Present Pay Scale & Pay

    areas_of_specialization = models.TextField(null=True) # Areas of Specialization and Current Interest

    additional_qualifications = models.TextField(null=True) # Additional Qualification acquired during the year

    pursuing_higher_studies = models.TextField(null=True) # Pursuing Higher Studies

    learning_methodology = models.TextField(null=True) # Participatory/Innovative Teaching Learning Methodologies used (give brief details )

    modifications_in_teaching = models.TextField(null=True) # Any Modification/ Addition to syllabus ( give brief details )

    beyond_syllabus = models.TextField(null=True) # Any Coverage/ Introduction beyond syllabus ( give brief details )

    # Number of Projects Guided

    projects_guided = models.PositiveIntegerField(null=True) # UG Projects Guided
    students_guided = models.PositiveIntegerField(null=True) # UG Students Guided

    # Contribution/Participation in Students Extra & Co-Curricular activities
    students_extra_curricular = models.TextField(blank=True)
    
    # Contribution/Participation in Departmental Activities & Development
    departmental_activities = models.TextField(blank=True)
    
    # Contribution/Participation in Institute Activities & Development
    institute_activities = models.TextField(blank=True)
    
    # Special/Extension/Expert/Invited Lectures Delivered
    invited_lectures = models.TextField(blank=True)
    
    # Articles, Monographs, Technical Reports, Reviews Written
    written_works = models.TextField(blank=True)




class Event(models.Model):
    attended_organized_choices = [
        ('Attended', 'Attended'),
        ('Organized', 'Organized'),
    ]

    form = models.ForeignKey(SelfAppraisalForm, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()

    # Sponsoring Agency and Organisation & Place held
    sponsoring_agency = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    place_held = models.CharField(max_length=200)
    
    attended_organized = models.CharField(max_length=10, choices=attended_organized_choices)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    form = models.ForeignKey(SelfAppraisalForm, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=20)
    course_title = models.CharField(max_length=200)
    contact_hours_per_week = models.PositiveIntegerField()
    total_hours_scheduled = models.PositiveIntegerField()
    total_hours_engaged = models.PositiveIntegerField()

    self_assessed_api_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    remarks = models.TextField(blank=True)
   
    def __str__(self):
        return f"{self.course_code} - {self.course_title}"

class KnowledgeResources(models.Model):
    form = models.ForeignKey(SelfAppraisalForm, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=20)
    resources_consulted = models.TextField()
    resources_prescribed = models.TextField()
    additional_resources_provided = models.TextField()
    self_assessed_api_score = models.DecimalField(max_digits=5, decimal_places=2)
    remarks = models.TextField()
  
    def __str__(self):
        return self.course_code
    

class EvaluationDuties(models.Model):

    def default_json():
        return {"UG": [0, 0, 0], "PG": [0, 0, 0]}

    def default_json_duties():
        return {"ALLOTED": [0, 0, 0], "Performed": [0, 0, 0]}

    form = models.ForeignKey(SelfAppraisalForm, on_delete=models.CASCADE)
    q_papers_set = models.JSONField(default=default_json)
    ab_evaluated = models.JSONField(default=default_json)
    students_examined = models.JSONField(default=default_json)
    invigilation_duties = models.JSONField(default=default_json_duties)
    api_score = models.IntegerField()
    hod_remarks = models.TextField()

    def __str__(self):
        return f"Activity: {self.activity.name}, Class: {self.class_type}"


class Publication(models.Model):
    form = models.ForeignKey(SelfAppraisalForm, on_delete=models.CASCADE)

    author_names = models.TextField(verbose_name="Names of All Authors in Order as in Publication")
    title_reference = models.TextField(verbose_name="Title and Complete Reference in IEEE Style")
    publication_type = models.CharField(max_length=100, verbose_name="Type of Publication/Conference etc.")
    api_score = models.PositiveIntegerField(blank=True, null=True, verbose_name="Self Assessed API Score")
    remarks = models.TextField(blank=True, null=True, verbose_name="Remarks by the HoD")

    def __str__(self):
        return f"Publication {self.serial_number}: {self.title_reference}"
    

class ResearchProject(models.Model):

    form = models.ForeignKey(SelfAppraisalForm, on_delete=models.CASCADE)

    title = models.CharField(max_length=200, verbose_name="Title of Research Project/Consultancy Work")
    sponsoring_agency = models.TextField(verbose_name="Details of Sponsoring Agency")
    duration_status = models.CharField(max_length=100, verbose_name="Duration, Sanction Date & Status")
    amount_sanctioned = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Amount Sanctioned")
    chief_investigator = models.CharField(max_length=100, verbose_name="Chief or Co Investigator Specify")
    api_score = models.PositiveIntegerField(blank=True, null=True, verbose_name="Self Assessed API Score")
    hod_remarks = models.TextField(blank=True, null=True, verbose_name="Remarks by the HoD")

    def __str__(self):
        return self.title

