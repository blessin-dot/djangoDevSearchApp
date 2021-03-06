from importlib.metadata import requires
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

def home(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/index.html', context)

def project(request, pk):
    projectObject = Project.objects.get(id=pk)
    context = {'project': projectObject}
    return render(request, 'projects/single_project.html', context)

def create_project(request):
    form =  ProjectForm()

    if request.method == 'POST':
        print(request.POST)
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form =  ProjectForm(instance=project)

    if request.method == 'POST':
        print(request.POST)
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)