from django.shortcuts import render
import requests
from .models import *
from works.models import *
from django.views.generic import DetailView



def index(request):
    return render(request, 'school_site/HTML/index.html', {'login': 'student_1', 'password': 'ertjjeigjirj'})

def main(request):
    subject = requests.get("http://cyberes.admin-blog.ru/LNTest/API/getItemCodeByFullName.php").json()
    works = requests.post("http://cyberes.admin-blog.ru/LNTest/API/Student/logIn.php",
                    data={'username': "student_1", 'password': 'e10adc3949ba59abbe56e057f20f883e'}).json()
    Works = WorksModel.objects.all()

    gfe = works.get('works')
    if gfe == Works:
        forks = 'yes'
    else:
        forks = 'hhhh'
    # for i,b in works.get('works').items():
    #     # print(i,b, len(b))
    #     for f in range(len(b)):
    #         work = WorksModel(i,b[f])
    #         work.save()
    subject_names = [*subject]
    bbe = {}

    data = {
        'subjects': subject_names,
        'done_works': works.get('CompletedWorks'),
        'bbe': bbe,
        'Works': Works,
        'forks': forks,
        'gfe': gfe,
    }
    return render(request, 'school_site/HTML/main.html', data)

class WorksDetailView(DetailView):
    model = WorksModel
    template_name = 'school_site/HTML/work_detail.html'
    context_object_name = 'work'
    subject = requests.get("http://cyberes.admin-blog.ru/LNTest/API/getItemCodeByFullName.php").json()
    subject_names = [*subject]
    bbe = {}
    data = {
        'subjects': subject_names,
        'bbe': bbe,
    }


def profile(request):
    user ={'info': requests.post("http://cyberes.admin-blog.ru/LNTest/API/Student/logIn.php",
                    data={'username': "student_1", 'password': 'e10adc3949ba59abbe56e057f20f883e'}).json()
           }
    return render(request, 'school_site/HTML/profile.html', user)


def testiruyu(request):
    works = requests.post("http://cyberes.admin-blog.ru/LNTest/API/Student/logIn.php",
                          data={'username': "student_1", 'password': 'e10adc3949ba59abbe56e057f20f883e'}).json()
    all_works = WorksModel.objects.all()
    for i, b in works.get('works').items():
        # print(i,b, len(b))
        for f in range(len(b)):
            if [i,b[f]] in all_works:
                break
            else:
                work = WorksModel(i, b[f])
                work.save()
    bbe = {}
    data = {
        'works': WorksModel.objects.all(),
        'bbe': bbe,
    }
    return render(request, 'school_site/HTML/testiruyu.html', data)