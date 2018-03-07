from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def chart(request):
    return render(request,"chart.html")
def doc(request):
    return render(request,"doc.html")