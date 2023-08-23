from django.db import models
from django.conf import settings


from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):

    # User Types
    USER_TYPE_CHOICES = (
        (1, 'HOD'),
        (2, 'Dean'),
        (3, 'VC'),
        (4, 'Faculty'),
    )

    department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True, blank=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=4)

class Department(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class SelfAppraisalForm(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Name
    
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True) # Department
    
    qualifications = models.CharField(verbose_name="3. Qualifications" ,max_length=100,null=True, blank=True) # Qualifications

    present_designation = models.CharField(verbose_name="4. Present Designation",max_length=100,null=True, blank=True) # Present Designation
    
    date_of_joining = models.DateField(verbose_name="5. University Joining Date",null=True, blank=True) # University Joining Date

    first_designation = models.CharField(verbose_name="6. First Designation",max_length=100,null=True, blank=True) # First Designation

    present_pay_scale_and_pay = models.CharField(verbose_name="7. Present Pay Scale & Pay",max_length=100,null=True, blank=True) # Present Pay Scale & Pay

    areas_of_specialization = models.TextField(verbose_name="8. Areas of Specialization and Current Interest",null=True, blank=True) # Areas of Specialization and Current Interest

    additional_qualifications = models.TextField(verbose_name="9. Additional Qualification acquired during the year (Give full details)",null=True, blank=True) # Additional Qualification acquired during the year

    pursuing_higher_studies = models.TextField(verbose_name="10. Pursuing Higher Studies (Give full details)",null=True, blank=True) # Pursuing Higher Studies

    learning_methodology = models.TextField(verbose_name="Participatory/Innovative Teaching Learning Methodologies used (give brief details)",null=True, blank=True)

    modifications_in_teaching = models.TextField(verbose_name="Any Modification/ Addition to syllabus (give brief details)",null=True, blank=True) 

    beyond_syllabus = models.TextField(verbose_name="Any Coverage/ Introduction beyond syllabus ( give brief details )",null=True, blank=True) 

    # Number of Projects Guided

    projects_guided = models.PositiveIntegerField(null=True, blank=True) # UG Projects Guided
    students_guided = models.PositiveIntegerField(null=True, blank=True) # UG Students Guided

    # Contribution/Participation in Students Extra & Co-Curricular activities
    students_extra_curricular = models.TextField(verbose_name="(A) Contribution/ Participation in Students Extra & Co- Curricular activities:",blank=True)
    
    # Contribution/Participation in Departmental Activities & Development
    departmental_activities = models.TextField(verbose_name="(B) Contribution/ Participation in Departmental Activities & Development:",blank=True)
    
    # Contribution/Participation in Institute Activities & Development
    institute_activities = models.TextField(verbose_name="(C) Contribution/ Participation in Institute Activities & Development:",blank=True)
    
    # Special/Extension/Expert/Invited Lectures Delivered
    invited_lectures = models.TextField(verbose_name="(D) Special/ Extension/ Expert/Invited Lectures Delivered, Give Details:",blank=True)
    
    # Articles, Monographs, Technical Reports, Reviews Written, Give Details:
    articles_monographs = models.TextField(verbose_name="(E) Articles, Monographs, Technical Reports, Reviews Written, Give Details:",blank=True)

    # 18. Membership of Professional Bodies/ National/ International Committees:
    # 19. Any Other Information:
    # 20. List of Enclosures:

    member_of_professional_bodies = models.TextField(blank=True)
    any_other_information = models.TextField(blank=True)
    list_of_enclosures = models.TextField(blank=True)


    # Fields to track the approval status
    self_approval = models.BooleanField(default=False)   # Means the form is filled by the user
    hod_approval = models.BooleanField(default=False)    # Checked by HOD
    # Overall Remarks of HoD:
    hod_remarks = models.TextField(blank=True)

    dean_approval = models.BooleanField(default=False)   # Approved by Dean
    # Overall Remarks of Dean:
    dean_remarks = models.TextField(blank=True)


    vc_approval = models.BooleanField(default=False)     # Approved by VC
    # Overall Remarks of VC:
    vc_remarks = models.TextField(blank=True)


    def __str__(self):
        return self.name.username
    

class Event(models.Model):
    attended_organized_choices = [
        ('Attended', 'Attended'),
        ('Organized', 'Organized'),
    ]

    form = models.ForeignKey(SelfAppraisalForm, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    # Sponsoring Agency and Organisation & Place held
    sponsoring_agency = models.CharField(max_length=200, null=True, blank=True)
    organization = models.CharField(max_length=200, null=True, blank=True)
    place_held = models.CharField(max_length=200, null=True, blank=True)
    
    attended_organized = models.CharField(max_length=10, choices=attended_organized_choices, null=True, blank=True)

    # by HOD
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    # TODO: ADD TYPE (ODD SEM OR EVEN SEM)
    course_type_choices = [
        (1, 'ODD SEM'),
        (2, 'EVEN SEM'),
    ]

    course_type = models.PositiveSmallIntegerField(choices=course_type_choices, default=1)

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
    self_assessed_api_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)
  
    def __str__(self):
        return self.course_code
    

class EvaluationDuties(models.Model):

    def default_json():
        return {"UG": [0, 0, 0], "PG": [0, 0, 0]}

    def default_json_duties():
        return {"ALLOTED": [0, 0, 0], "Performed": [0, 0, 0]}

    form = models.OneToOneField(SelfAppraisalForm, on_delete=models.CASCADE)
    q_papers_set = models.JSONField(default=default_json, null=True, blank=True)
    ab_evaluated = models.JSONField(default=default_json, null=True, blank=True)
    students_examined = models.JSONField(default=default_json, null=True, blank=True)
    invigilation_duties = models.JSONField(default=default_json_duties, null=True, blank=True)
    api_score = models.IntegerField(null=True, blank=True)
    hod_remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"form: {self.form}"


class Publication(models.Model):
    publication_choices = [
        (1, 'Research Papers Published/ Presented'),
        (2, 'Books, Chapters in Books Written'),
    ]

    publication_choice = models.PositiveSmallIntegerField(choices=publication_choices)
    form = models.ForeignKey(SelfAppraisalForm, on_delete=models.CASCADE)

    author_names = models.TextField(verbose_name="Names of All Authors in Order as in Publication")
    title_reference = models.TextField(verbose_name="Title and Complete Reference in IEEE Style")
    publication_type = models.CharField(max_length=100, verbose_name="Type of Publication/Conference etc.")
    api_score = models.PositiveIntegerField(blank=True, null=True, verbose_name="Self Assessed API Score")
    remarks = models.TextField(blank=True, null=True, verbose_name="Remarks by the HoD")

    def __str__(self):
        return f"Publication {self.title_reference}"
    

class ResearchProject(models.Model):

    form = models.ForeignKey(SelfAppraisalForm, on_delete=models.CASCADE)

    title = models.CharField(max_length=200, verbose_name="Title of Research Project/Consultancy Work",null=True, blank=True)
    sponsoring_agency = models.TextField(verbose_name="Details of Sponsoring Agency",null=True, blank=True)
    duration = models.CharField(verbose_name="Duration", max_length=100,null=True, blank=True)
    # Sanction Date & Status
    sanction_date = models.DateField(verbose_name="Sanction Date",null=True, blank=True)

    # TODO: MAKE THIS BOOLEEN FIELD
    status = models.CharField(max_length=100, verbose_name="Status",null=True, blank=True)

    amount_sanctioned = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Amount Sanctioned",null=True, blank=True)
    chief_investigator = models.CharField(max_length=100, verbose_name="Chief or Co Investigator Specify",null=True, blank=True)
    
    
    api_score = models.PositiveIntegerField(blank=True, null=True, verbose_name="Self Assessed API Score")
    remarks = models.TextField(blank=True, null=True, verbose_name="Remarks by the HoD")

    def __str__(self):
        return self.title


class ResearchGuidance(models.Model):
    level_choices = [
        ('PhD', 'PhD'),
        ('DD', 'DD'),
        ('M Tech', 'M Tech'),
        ('M Phil', 'M Phil'),
        ('MS', 'MS'),
    ]

    status_choices = [
        ('Completed', 'Completed'),
        ('Ongoing', 'Ongoing'),
    ]

    form = models.ForeignKey(SelfAppraisalForm, on_delete=models.CASCADE)

    enrollment_number = models.CharField(max_length=100, verbose_name="Enrollment Number")
    name_of_student = models.CharField(max_length=100, verbose_name="Name of the Student")
    title_of_thesis = models.CharField(max_length=200, verbose_name="Title of Thesis/Dissertation/Project")
    names_of_joint_supervisors = models.CharField(max_length=200, verbose_name="Names of Joint Supervisors")
    level = models.CharField(max_length=100, choices=level_choices, verbose_name="Level")
    status = models.CharField(max_length=100, choices=status_choices, verbose_name="Status")


    api_score = models.PositiveIntegerField(blank=True, null=True, verbose_name="Self Assessed API Score")
    remarks = models.TextField(blank=True, null=True, verbose_name="Remarks by the HoD")


    def __str__(self):
        return self.title_of_thesis
