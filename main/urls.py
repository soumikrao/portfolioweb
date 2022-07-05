from django.urls import path, include
from . import views
from .views import ProjectView, ProjectPost, GAView, GAPost

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about),
    path("skills/", views.skills),
    path("projects/", ProjectView.as_view(), name="project"),
    path("goalachieve/", GAView.as_view(), name="achievemnts"),
    path("achieveupdate/", GAPost.as_view(), name="achievemnts"),
    path("projectupdate/", ProjectPost.as_view(), name="projectpost"),
]