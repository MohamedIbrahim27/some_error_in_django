from django.shortcuts import render

# Create your views here.
from.models import ModelName



def name(request):
    if request.method =='POST':
        firtst=request.POST['nameasdasda']
        n=ModelName.objects.create(name=firtst)
    return render(request,'main.html')