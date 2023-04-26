from django.shortcuts import render, redirect
from works.models import *
from .forms import *

# Create your views here.
def main(request):
    if request.method == 'POST':
        form = WorksCreateForm(request.POST)
        if form.is_valid():
            print(form.data)
    form = WorksCreateForm()
    return render(request, 'school_site/HTML/obriumteach.html', {"form": form})

def profile(request):
    login = request.session.get('teacher')['login']
    password = request.session.get('teacher')['password']
    teacher = {'teacher': requests.post("http://cyberes.admin-blog.ru/LNTest/API/Student/logIn.php",
                    data={'username': login, 'password': password}).json()}
    return render(request, 'school_site/HTML/acc.html', teacher)