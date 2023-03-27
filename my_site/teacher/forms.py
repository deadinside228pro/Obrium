from django.forms import *
from works.models import *

class WorksCreateForm(ModelForm):
    class Meta:
        model = WorksModel
        fields = ['name', 'theme']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'имя работы'
            }),
            "theme": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'тема работы'
            })
        }