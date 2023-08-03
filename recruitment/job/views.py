#
#recruitment_app/views.py
from django.shortcuts import render, redirect
from .models import JobPost
from .forms import JobPostForm, CandidateApplicationForm

def home(request):
    # Fetch recent job postings for the front page
    recent_job_postings = JobPost.objects.order_by('-posted_date')


    if request.method == 'POST':
        job_form = JobPostForm(request.POST)
        application_form = CandidateApplicationForm(request.POST, request.FILES)
        
        if job_form.is_valid():
            job_form.save()
            return redirect('home')
        
        if application_form.is_valid():
            application_form.save()
            return redirect('home')
    else:
        job_form = JobPostForm()
        application_form = CandidateApplicationForm()

    context = {
        'recent_job_postings': recent_job_postings,
        'job_form': job_form,
        'application_form': application_form,
    }
    return render(request, 'job/home.html', context)
