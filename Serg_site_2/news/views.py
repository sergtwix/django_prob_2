from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print(request)
    return HttpResponse('Hlow World1')


def test(request):
    print(request)
    return HttpResponse('<h1>Сторінка ТЕСТ_1</h1>')

