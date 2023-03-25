from django.shortcuts import render

def tests(request):
    return render(request, 'tests/all_tests.html')