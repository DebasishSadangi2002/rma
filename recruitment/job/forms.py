# recruitment_app/forms.py
from django import forms
from .models import JobPost, CandidateApplication

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ['title', 'description', 'skills_required', 'location','salary']

class CandidateApplicationForm(forms.ModelForm):
    class Meta:
        model = CandidateApplication
        fields = ['job_post', 'candidate_name', 'email', 'resume']
