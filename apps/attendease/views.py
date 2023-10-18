from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "base.html")

def practice(request):
    return render(request, "practice.html")

def lecdashcl(request):
    return render(request, "lecdashcl.html")

def lechistory(request):
    return render(request, "lechistory.html")

def schedlec(request):
    return render(request, "schedlec.html")
