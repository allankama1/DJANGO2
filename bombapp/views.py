from django.shortcuts import render

# Create your views here.
def liverpool(request):
    return render(request,'liverpool club.html')

def mat(request):
    return render(request,'matwana culture.html')

def muscle(request):
    return render(request,'trackhawks.html')