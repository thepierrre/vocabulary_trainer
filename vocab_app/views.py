from http import HTTPStatus
from http.client import HTTPResponse
import random
from django.shortcuts import render
import pandas as pd

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
    question_set = QuestionSet.objects.filter(slug=list).first()
    questions = Question.objects.filter(set__slug=list)
    if request.method == 'POST':
        correct = 0
        percentage = 6
        for q in questions:
            q.user_answer = request.POST.get(q.question)
            q.user_answer_article = request.POST.get(f'{q.question}_article')
            if q.user_answer == q.answer and (q.article == q.user_answer_article or q.is_noun == False):
                q.correct = True
                correct += 1
            else:
                q.correct = False
        percentage = round(correct / len(questions) * 100)
        return render(
            request, 
            "vocab_app/vocabulary_list.html", 
            { 
                "list_title": question_set.topic_name,
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
            { 
                "list_title": question_set.topic_name,
                "questions": questions 
            }
        )


def upload_csv(request, language):
    if request.method == 'POST':
        try:
            csv_file = request.FILES['file']
            questions = pd.read_csv(csv_file, delimiter=';', na_filter=False).to_dict('index')
            list_name = request.POST['title']
            if QuestionSet.objects.filter(topic_name=list_name).count() == 0:
                new_list = QuestionSet.objects.create(topic_name=list_name, 
                                                        questions_language=LanguageChoices.ENGLISH, 
                                                        answer_language=language)
                for question in questions.values():
                    question_data = {k: v for k, v in question.items()}
                    Question.objects.create(set=new_list, **question_data)
            return render(
                request, 
                "vocab_app/language.html", 
                { "language": language, "lists": QuestionSet.objects.filter(answer_language=language) }
            )
        except Exception as e:
            print(e)
            return render(
                request, 
                "vocab_app/vocabulary_list_csv_form.html", 
                { "language": language }
            )
    return render (
        request, 
        "vocab_app/vocabulary_list_csv_form.html", 
        { "language": language }
    )
    
    