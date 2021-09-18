from django.shortcuts import render
from teacher.models import Subject 


def createSubject(request):
    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return render(request, "teacher/lesson_create.html", {"form":form })


def viewSubject(request):
    subjects = Subject.objects.all()
    return render(request, "teacher/lesson_list_view.html", {"subjects":subjects })

def viewSubjectDetails(request, id):
    subjects = Subject.objects.get(id=id)
    return render(request, "teacher/lesson_detail_view.html", {"subjects":subjects })


def updateSubject(request, id):
    subject = Subject.objects.get(id=id)
    form = LessonForm(instance=subject)
     if request.method == "POST":
        form = LessonForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subject_details')
        else:
            print(form.error)
    return render(request, "teacher/lesson_update.html", {"form":form })


def deleteSubject(request, id)
    Subject.objects.filter(id=id).delete()
    return redirect('subject_details')
