from django.http import HttpResponse
from django.shortcuts import render
from uploadapp.models import studenttable
from viewattendance.models import Classroom, Course, Attendance, Student


def index(request):
    if request.method == 'POST':
        classname = request.POST['class']
        course = request.POST['course']
        sdate = request.POST['sdate']
        edate = request.POST['edate']
        if classname == "" or course == "" or sdate == "" or edate == "":
            context = dict()
            context['classoptions'] = [str(elem[0]) for elem in list(Classroom.objects.all().values_list('class_id'))]
            context['courseoptions'] = [str(elem[0]) for elem in list(Course.objects.all().values_list('course_id'))]
            context['error'] = True
            return render(request, 'reporthome.html', context)
        classid = Classroom.objects.get(class_id=classname)
        ans = Attendance.objects.filter(class_id=classid)
        for elem in ans:
            print(elem)
        return HttpResponse("graph")
    context = dict()
    context['classoptions'] = [str(elem[0]) for elem in list(Classroom.objects.all().values_list('class_id'))]
    context['courseoptions'] = [str(elem[0]) for elem in list(Course.objects.all().values_list('course_id'))]
    return render(request, 'reporthome.html', context)
