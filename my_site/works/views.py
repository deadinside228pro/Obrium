from django.shortcuts import render

def tests(request):
    return render(request, 'works/all_tests.html')