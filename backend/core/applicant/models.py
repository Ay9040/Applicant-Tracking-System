from django.db import models
from core.user.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from core.Resume_Parser.Parser import resume_result_wrapper, process

def Parse(filename):
    text = resume_result_wrapper(filename)
    text = process(text)
    return text


class ApplicantDetails(models.Model):
    class ApplicantObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset()
    
        def create_applicant_details(
            self, 
            applicant_id,
            resume,
            preferred_location,
            job_categories,
            parsed_resume,
            **kwargs
        ):
            if applicant_id is None:
                raise TypeError(
                    "Education details must be associated with an applicant."
                    )

            applicant_details = self.model(
                applicant_id=applicant_id,
                resume=resume,
                preferred_location=preferred_location,
                job_categories=job_categories,
                parsed_resume=parsed_resume,
            )
            applicant_details.save(using=self._db)
            filename = 'resumes/' + applicant_details.resume.name
            ApplicantDetails.applicant_objects.filter(applicant_id=applicant_details.applicant_id).update(parsed_resume=Parse(filename))
            return applicant_details
    
    applicant_id = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to ='resumes/', default='settings.MEDIA_ROOT/resumes/Mihir Mehta Resume.pdf') # MEDIA_ROOT/resumes
    PREFERRED_LOCATION_CHOICES = [("CA", "California"), ("NYC", "New York City"), ("IL", "Chicago"), ("WS", "Seattle"), ("BO", "Boulder")]
    preferred_location = models.CharField(max_length=50, choices=PREFERRED_LOCATION_CHOICES, default="CA")
    JOB_CATEGORIES_CHOICES = [("SWE", "Software Engineer"), ("FE", "Frontend Engineer"), ("BE", "Backend Engineering"), ("D", "Devops"), ("ML", "Machine Learning Engineer")]
    job_categories = models.CharField(max_length=3, choices=JOB_CATEGORIES_CHOICES, default="SWE")
    parsed_resume = models.CharField(max_length=10485760, default=None, null=True)
    objects = models.Manager()
    applicant_objects = ApplicantObjects()

    def __str__(self):
        return self.applicant_id.first_name