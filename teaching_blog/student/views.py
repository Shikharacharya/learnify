from django.shortcuts import render
from teacher.models import Subject 


def subject(request):
    subjects = Subject.objects.all()
    return render(request, "user/lesson_list_view.html", {"subjects":subjects })