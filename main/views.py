from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import projects, achievements

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def skills(request):
    return render(request, 'main/skills.html')

def projectupdate(request):
    return render(request, 'main/projectupdate.html')

class GAView(ListView):
    model = achievements
    template_name = 'main/ga.html'

class GAPost(CreateView):
    model = achievements
    template_name = 'main/achievementupdate.html'
    fields = '__all__'


class ProjectView(ListView):
    model = projects
    template_name = 'main/projects.html'

class ProjectPost(CreateView):
    model = projects
    template_name = 'main/projectupdate.html'
    fields = '__all__'