from django.urls import path

from . import views

urlpatterns = [
    path("",
        views.starting_page,
        name="starting-page"),
    path("languages",
        views.languages,
        name="languages-page"),
    path("log-in",
        views.log_in,
        name="log-in"),
    path("about",
        views.about,
        name="about"),
    path("languages/<slug:language>",
        views.language_list,
        name="language-list"),
    path ("languages/<slug:language>/<slug:list>",
        views.vocabulary_list,
        name="list-detail-page"),
]
