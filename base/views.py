from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Skill
from .forms import SkillForm


def home(request):
    return render(request, 'home.html')


def skills(request):
    skill_set = Skill.objects.all()

    context = {
        'skills': skill_set
    }

    return render(request, 'skills.html', context)

def skill(request, pk):
    skill = Skill.objects.get(id=pk)

    context = {
        'skill': skill
    }

    return render(request, 'skill.html', context)

def createSkill(request):
    form = SkillForm()
    context = { 'form': form }

    if request.method == 'POST':
        form = SkillForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('skills')

    return render(request, 'create-skill.html', context)

def updateSkill(request, pk):
    skill = Skill.objects.get(id=pk)
    form = SkillForm(instance=skill)
    context = {'form': form}

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)

        if form.is_valid():
            form.save()

            return redirect('skills')

    return render(request, 'create-skill.html', context)

def deleteSkill(request, pk):
    skill = Skill.objects.get(id=pk)

    if request.method == 'POST':
        skill.delete()

        return redirect('skills')

    context = {
        'skill': skill
    }

    return render(request,'delete-skill.html', context)