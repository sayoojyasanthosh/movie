
from django.shortcuts import render
from film.models import Filmview
from film.forms import movieform
# Create your views here.

def home(request):
    f=Filmview.objects.all()
    return render(request,'home.html',{'f':f})
def film(request):
    if(request.method=="POST"):
        n=request.POST['n']
        d=request.POST['d']
        y=request.POST['y']
        p=request.FILES['p']
        f=Filmview.objects.create(name=n,desc=d,year=y,image=p)
        f.save()
        return home(request)
    return render(request,'addmovie.html')


def viewdetail(request,p):
    f=Filmview.objects.get(name=p)
    return render(request, 'view.html',{'f':f})


def delete(request,p):
    f=Filmview.objects.get(name=p)
    f.delete()
    return home(request)

def update(request,p):
    f=Filmview.objects.get(name=p)
    form=movieform(instance=f)

    if(request.method=="POST"):
        form=movieform(request.POST,instance=f)
        if form.is_valid():
           form.save()
           return viewdetail(request,p)
    return render(request, 'update.html',{'form':form})