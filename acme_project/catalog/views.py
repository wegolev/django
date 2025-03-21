from django.shortcuts import render, HttpResponse

# Create your views here.
# def index(request):
#     return render(request, 'homepage/index.html')


def index(request):
    return HttpResponse('<h1>Здесь же была ракета!</h1>')
