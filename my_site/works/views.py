from django.shortcuts import render


def tests(request):
    return render(request, 'works/HTML/all_tests.html')



