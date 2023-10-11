from django.shortcuts import render # origineel
from django.shortcuts import render, redirect, get_object_or_404 # volgens tutorial
from django.utils import timezone

# Create your views here.
from .models import Werken

# Create your views here.
def home(request):
    werken = Werken.objects
    return render(request, 'werken/werken.html', {'werken': werken})

def detail(request, werken_id):
    werk = get_object_or_404(Werken, pk=werken_id)
    return render(request, 'werken/detail.html', {'werk': werk})


def create(request):
    if request.method == 'POST':
        if  request.POST['title'] and \
            request.POST['body'] and \
            request.POST['url']:
            werk = Werken()
            werk.title = request.POST['title']
            werk.body = request.POST['body']

            if  request.POST['url'].startswith('http://') or \
                request.POST['url'].startswith('https://'):
                    werk.url= request.POST['url']
            else:
                werk.url='http://' + request.POST['url']

            # werk.icon = request.FILES['icon']
            # werk.image = request.FILES['image']
            # if request.FILES['image']:
            #     werk.image = request.FILES['image']
            # if request.FILES['icon']:
            #     werk.icon = request.FILES['icon']

            werk.image = request.FILES.get('image', None)
            werk.icon = request.FILES.get('icon', None)

            werk.pub_date = timezone.datetime.now()
            werk.hunter = request.user
            # if request.user.is_authenticated:
            #     werk.hunter = request.user


            werk.save()
            return redirect ('/werken/' + str(werk.id))
        else:
            return render(request,'werken/toevoegen.html', {'error':'niet \ alle velden zijn ingevuld.'})
    else:
        return render(request,'werken/toevoegen.html')