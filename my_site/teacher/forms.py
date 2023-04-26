import requests
from django import forms
from requests import *
from works.models import *

subjects = requests.post("http://cyberes.admin-blog.ru/LNTest/API/getItemCodeByFullName.php").json()

subjects = tuple(map(lambda x: (x[1], x[0]), subjects.items()))

class WorksCreateForm(forms.Form):
    subject = forms.ChoiceField(choices=subjects)
