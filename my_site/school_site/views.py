from django.shortcuts import render
import requests
from .models import *
from works.models import *



def index(request):
    return render(request, 'school_site/HTML/index.html', {'login': 'student_1', 'password': 'ertjjeigjirj'})

def main(request):
    subject = requests.get("http://cyberes.admin-blog.ru/LNTest/API/getItemCodeByFullName.php").json()
    works = requests.post("http://cyberes.admin-blog.ru/LNTest/API/Student/logIn.php",
                    data={'username': "student_1", 'password': 'e10adc3949ba59abbe56e057f20f883e'}).json()
    subject_names = [*subject]
    bbe = {}
    Works = WorksModel.objects.all()
    data = {
        'subjects': subject_names,
        'works': works.get('works'),
        'done_works': works.get('CompletedWorks'),
        'bbe': bbe,
        'Works': Works,
    }
    return render(request, 'school_site/HTML/main.html', data)

def profile(request):
    user ={'info': requests.post("http://cyberes.admin-blog.ru/LNTest/API/Student/logIn.php",
                    data={'username': "student_1", 'password': 'e10adc3949ba59abbe56e057f20f883e'}).json()
           }
    return render(request, 'school_site/HTML/profile.html', user)