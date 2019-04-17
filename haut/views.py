from django.shortcuts import render
from django.http  import HttpResponse
# Create your views here.
def home(request):
    return render(request,'index.html')
def mission(request):
    return render(request,'mission.html')
def promoter(request):
    return render(request,'promoters.html')
def campuse(request):
    return render(request,'campuses.html')