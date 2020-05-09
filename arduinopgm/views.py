from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .arduinoloader import adloader
import sqlite3


def hwhome(request):
    if request.method == 'POST':
        logout(request)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/hardware/home')
        return render(request, 'hardwarelogin.html', {'error': True})
    return render(request, 'hardwarelogin.html', {})


@login_required(login_url='/hardware/')
def home(request):
    database = "./db.sqlite3"
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        query = "SELECT class_id FROM 'viewattendance_classroom'"
        cur.execute(query)
    except:
        return render(request, 'hardwarehome.html', {"error": True})
    rows = cur.fetchall()  # [0][0]
    cls = rows
    return render(request, 'hardwarehome.html', {"class": cls})


@login_required(login_url='/hardware/')
def loggingout(request):
    logout(request)
    return redirect('hwhome')


@login_required(login_url='/hardware/')
def clear(request):
    adloader(1, "")
    return redirect('home')


@login_required(login_url='/hardware/')
def enroll(request):
    adloader(2, "")
    return redirect('home')


@login_required(login_url='/hardware/')
def record(request):
    cls = request.GET['class']
    adloader(3, cls)
    return redirect('home')
