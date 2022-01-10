import random
from django.shortcuts import render

from .models import LanguageChoices, QuestionSet, Question

# Create your views here.

welcomes = [
    { "text": "Hello", "color": "darkred" }, 
    { "text": "Bonjour", "color": "skyblue" }, 
    { "text": "Hallo", "color": "green" }, 
    { "text": "Ahoj", "color": "navy" },
    { "text": "Servus", "color": "saddlebrown" },
    { "text": "Ola", "color": "chocolate" },
    { "text": "Hola", "color": "moccasin" },
    { "text": "Ciao", "color": "indianred" },
    { "text": "Hoi", "color": "lightsalmon" },
    { "text": "Hei", "color": "mediumpurple" },
    { "text": "Cześć", "color": "yellowgreen" },
]

def starting_page(request):
    return render(request, "vocab_app/index.html", { "welcome": random.choice(welcomes) })

def languages(request):
    return render (request, "vocab_app/languages.html")

def log_in(request):
    return render (request, "vocab_app/log-in.html")

def about(request):
    return render (request, "vocab_app/about.html")

# def language_detail(request):
#     pass

def language_list(request, language):
    return render (
        request, 
        "vocab_app/language.html", 
        { "language": language, "lists": QuestionSet.objects.filter(answer_language=language) }
    )

def vocabulary_list(request, language, list):
    questions = Question.objects.filter(set__slug=list)
    if request.method == 'POST':
        correct = 0
        percentage = 6
        for q in questions:
            q.user_answer = request.POST.get(q.question)
            q.user_answer_article = request.POST.get(f'{q.question}_article')
            if q.user_answer == q.answer and q.article == q.user_answer_article or q.is_noun == False:
                q.correct = True
                correct += 1
            else:
                q.correct = False
        percentage = round(correct / len(questions) * 100)
        return render(
            request, 
            "vocab_app/vocabulary_list.html", 
            { 
                "questions": questions,
                "result": {
                    "correct": correct,
                    "percentage": percentage,
                }
            }
        )
    else:
        return render(
            request, 
            "vocab_app/vocabulary_list.html", 
            { "questions": questions }
        )