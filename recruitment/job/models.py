# recruitment_app/models.py
from django.db import models

class JobPost(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    skills_required = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    posted_date = models.DateTimeField(auto_now_add=True)
    salary = models.IntegerField()

class CandidateApplication(models.Model):
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    candidate_name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    applied_date = models.DateTimeField(auto_now_add=True)
    def job_post_title(self):
        return self.job_post.title
