from django.shortcuts import render
import requests


def index(request):
    return render(request, 'school_site/HTML/index.html', {'login': 'student_1', 'password': 'ertjjeigjirj'})

def main(request):
    subject = requests.get("http://cyberes.admin-blog.ru/LNTest/API/getItemCodeByFullName.php").json()
    data = {
        'subjects': subject,
        'need_sub': [i for i in subject.keys()]
    }
    return render(request, 'school_site/HTML/main.html', data)

def profile(request):
    return render(request, 'school_site/HTML/profile.html')