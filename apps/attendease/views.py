from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "attendease/homepage.html")

def dashboard(request):
    return render(request, "dashboard/base.html")
