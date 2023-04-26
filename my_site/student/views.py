import requests
from django.shortcuts import render

def main(request):
    print(request.session.get('student')['login'])
    login = request.session.get('student')['login']
    password = request.session.get('student')['password'] # e10adc3949ba59abbe56e057f20f883e
    subject = requests.get("http://cyberes.admin-blog.ru/LNTest/API/getItemCodeByFullName.php").json()
    student = requests.post("http://cyberes.admin-blog.ru/LNTest/API/Student/logIn.php",
                    data={'username': login, 'password': password}).json()
    # Works = WorksModel.objects.all()
    works = student.get('works')
    # if gfe == Works:
    #     forks = 'yes'
    # else:
    #     forks = 'hhhh'
    # for i,b in works.get('works').items():
    #     # print(i,b, len(b))
    #     for f in range(len(b)):
    #         work = WorksModel(i,b[f])
    #         work.save()
    subject_names = [*subject]

    data = {
        'subjects': subject_names,
        'done_works': student.get('CompletedWorks'),
        'student': student,
        'forks': 'forks',
        'works': works,
    }
    return render(request, 'school_site/HTML/obrium.html', data)