from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,"iplteams/index.html")
def CSK(request):
    return render(request,"iplteams/CSK.html")
def DC(request):
    return render(request,"iplteams/DC.html")
def GT(request):
    return render(request,"iplteams/GT.html")
def KKR(request):
    return render(request,"iplteams/KKR.html")
def LSG(request):
    return render(request,"iplteams/LSG.html")
def MI(request):
    return render(request,"iplteams/MI.html")
def PBKS(request):
    return render(request,"iplteams/PBKS.html")
def RCB(request):
    return render(request,"iplteams/RCB.html")
def RR(request):
    return render(request,"iplteams/RR.html")
def SRH(request):
    return render(request,"iplteams/SRH.html")