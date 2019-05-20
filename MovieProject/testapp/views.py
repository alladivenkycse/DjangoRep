from django.shortcuts import render
from testapp.forms import MovieForm
from testapp.models import Movie
# Create your views here.
def Movie_Dashboard(request):
    return render(request,'testapp/index.html')
def Movie_Add(request):
    form=MovieForm()
    if(request.method=='POST'):
        form=MovieForm(request.POST)
        if(form.is_valid()):
            form.save()
            #=MovieForm()
            return Movie_Dashboard(request)

    return render(request,'testapp/Movieadd.html',{'form':form})

def Movie_list(request):
    movielist=Movie.objects.all().order_by('-id')
    return render(request,'testapp/listmovie.html',{'form':movielist})
