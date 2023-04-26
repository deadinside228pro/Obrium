from django.shortcuts import render, redirect
import requests

from django.conf import settings
from .forms import RegForm
from works.models import *
from django.views.generic import DetailView


def reg(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            if not form.data.get('teacher_check'):
                student = requests.post("http://cyberes.admin-blog.ru/LNTest/API/Student/logIn.php",
                                        data={'username': f"{form.cleaned_data.get('login')}",
                                              'password': f"{form.cleaned_data.get('password')}"}).json()
                print(student)
                if student == 1337:
                    form.errors['reg_error'] = 'неправильный логин или пароль'
                    print(form.errors.get('reg_error'))
                    return render(request, 'school_site/HTML/obriumreg.html', {'form': form})
                else:
                    reg_data = {'login': form.cleaned_data.get('login'), 'password': form.cleaned_data.get('password')}
                    request.session[settings.STUDENT_SESSION_ID] = reg_data
                    return redirect('/student/main')
            else:
                teacher = requests.post("http://cyberes.admin-blog.ru/LNTest/API/Teacher/logInTeacher.php",
                                        data={'username': f"{form.cleaned_data.get('login')}",
                                              'password': f"{form.cleaned_data.get('password')}"}).json()
                if teacher == 1337:
                    form.errors['reg_error'] = 'неправильный логин или пароль'
                    return render(request, 'school_site/HTML/obriumreg.html', {'form': form})
                else:
                    reg_data = {'login': form.cleaned_data.get('login'),
                                'password': form.cleaned_data.get('password')}
                    request.session[settings.TEACHER_SESSION_ID] = reg_data
                    return redirect('/teacher/main')
    else:
        form = RegForm()
    return render(request, 'school_site/HTML/obriumreg.html', {'form': form})


# def main(request):
#     print(request.session.get('student')['login'])
#     login = request.session.get('student')['login']
#     password = request.session.get('student')['password']  # e10adc3949ba59abbe56e057f20f883e
#     subject = requests.get("http://cyberes.admin-blog.ru/LNTest/API/getItemCodeByFullName.php").json()
#     student = requests.post("http://cyberes.admin-blog.ru/LNTest/API/Student/logIn.php",
#                             data={'username': login, 'password': password}).json()
#     # Works = WorksModel.objects.all()
#     works = student.get('works')
#     # if gfe == Works:
#     #     forks = 'yes'
#     # else:
#     #     forks = 'hhhh'
#     # for i,b in works.get('works').items():
#     #     # print(i,b, len(b))
#     #     for f in range(len(b)):
#     #         work = WorksModel(i,b[f])
#     #         work.save()
#     subject_names = [*subject]
#
#     data = {
#         'subjects': subject_names,
#         'done_works': student.get('CompletedWorks'),
#         'student': student,
#         'forks': 'forks',
#         'works': works,
#     }
#     return render(request, 'school_site/HTML/obrium.html', data)


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


# def profile(request):
#     login = request.session.get('student')['login']
#     password = request.session.get('student')['password']
#     student = {'student': requests.post("http://cyberes.admin-blog.ru/LNTest/API/Student/logIn.php",
#                                         data={'username': login, 'password': password}).json()}
#     return render(request, 'school_site/HTML/acc.html', student)


def testiruyu(request):
    works = requests.post("http://cyberes.admin-blog.ru/LNTest/API/Student/logIn.php",
                          data={'username': "student_1", 'password': 'e10adc3949ba59abbe56e057f20f883e'}).json()
    all_works = WorksModel.objects.all()
    for i, b in works.get('works').items():
        # print(i,b, len(b))
        for f in range(len(b)):
            if [i, b[f]] in all_works:
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
