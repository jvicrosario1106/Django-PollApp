from django.shortcuts import render,redirect
from .models import Question,Choice
from django.contrib import messages
# Create your views here.

def home(request):
    question = Question.objects.all()
    messages.success(request, " | Vote Now!")
    return render(request, 'pollapp/home.html', {'question':question})

def vote(request, pk):
    question = Question.objects.get(id=pk)
    try:
        choice = question.choice_set.get(id=request.POST['choice'])
    except(KeyError):
        print("Failed to vote")

    else:
        choice.votes +=1
        choice.save()
        messages.success(request, " You Successfully Vote")
        return redirect("home")

    return render(request, 'pollapp/vote.html', {'question':question})

def result(request, pk):
    question = Question.objects.get(id = pk)
    return render(request, 'pollapp/results.html', {'question':question})

