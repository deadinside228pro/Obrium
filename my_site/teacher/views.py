from django.shortcuts import render, redirect
from works.models import *
from .forms import *

# Create your views here.
def teacher_main(request):
    err = ''
    if request.method == 'POST':
        form = WorksCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            err = 'НЕВерНЫе Данные'
    excrs = ExcsModel.objects.all()
    form = WorksCreateForm()
    data = {
        'excrs': excrs,
        'form': form,
        'err': err
    }
    return render(request, 'teacher/teacher_main.html', data)
