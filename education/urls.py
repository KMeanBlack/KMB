from django.urls import path
from . import views

urlpatterns = [
    path("", views.education, name='Education'),
    path("student", views.student, name="student"),
    path("student/<int:myid>", views.studentView, name="studentView"),
    path("teachers", views.teachers, name="Teachers"),
    path('search', views.search, name="search"),
    ]