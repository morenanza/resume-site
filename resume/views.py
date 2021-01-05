from django.shortcuts import render
from django.http import FileResponse
from .models import Resume, Skill, Education, Experience

# Create your views here.

def home(request):
    context = {
        'title': "home"
    }
    return render(request, 'resume/home.html', context)

def about(request):
    context = {
        'title': "about",
        'resume': Resume.objects.get(pk=1),
        'skills': Skill.objects.filter(resume_id=1).order_by("-percentage"),
        'experiences': Experience.objects.filter(resume_id=1),
        'educations': Education.objects.filter(resume_id=1)
    }
    return render(request, 'resume/about.html',context)

def blog(request):
    context = {
        'title': "blog"
    }
    return render(request, 'resume/blog.html',context)

def download(request):
    resume = Resume.objects.get(pk=1)
    filename = resume.cv.path
    response = FileResponse(open(filename, 'rb'))
    return response
