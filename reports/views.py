from django.shortcuts import render
from viewattendance.models import Classroom, Course, Attendance
import plotly
import plotly.graph_objects as go
import pandas as pd


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
        courseid = Course.objects.get(course_id=course)
        title = "Graph for "+course+" of "+classname+" from " + sdate + " to " + edate
        dmy = sdate.split('/')
        sdate = dmy[2] + "-" + dmy[1] + "-" + dmy[0]
        dmy = edate.split('/')
        edate = dmy[2] + "-" + dmy[1] + "-" + dmy[0]
        resultset = Attendance.objects.filter(class_id=classid, course_id=courseid, date__gte=sdate, date__lte=edate)
        df = pd.DataFrame.from_records(
            resultset.all().values_list('student_id', 'date', 'status', 'hour'))
        if df.empty:
            with open("./templates/report.html", 'w') as f:
                f.write("<h2><center>No enough data to generate graph</center></h2>")
            return render(request, 'report.html', {})
        df[1] = df[1].astype(str)+" Hour:"+df[3].astype(str)
        dateandhour = df[1].unique()
        present = []
        absent = []
        for elem in dateandhour:
            temp = df[df[1] == elem]
            temp = temp[2].value_counts()
            try:
                present.append(temp["Present"])
            except:
                present.append(0)
            try:
                absent.append(temp["Absent"])
            except:
                absent.append(0)
        fig = go.Figure(data=[
            go.Bar(name='Present', x=dateandhour, y=present, marker_color="green"),
            go.Bar(name='Absent', x=dateandhour, y=absent, marker_color="red")])
        fig.update_layout(
            barmode='stack', title=title,
            xaxis_title="Date and Hour", yaxis_title="Total Students",
            font=dict(family="Courier New, monospace", size=24, color="#0f0f0f"))
        plotly.offline.plot(fig, filename='./templates/report.html', auto_open=False)
        return render(request, 'report.html', {})
    context = dict()
    context['classoptions'] = [str(elem[0]) for elem in list(Classroom.objects.all().values_list('class_id'))]
    context['courseoptions'] = [str(elem[0]) for elem in list(Course.objects.all().values_list('course_id'))]
    return render(request, 'reporthome.html', context)
