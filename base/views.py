from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views1 here.

from base.models import Room


def hello(request):
    s = request.GET.get('s', ' ')
    return HttpResponse(f"Hello {s}")

def search(request):
    q = request.GET.get('q', ' ')
    if q == ' ' :
            return HttpResponse("Zadejte co chcete hledat")
    else:
        rooms = Room.objects.filter(Q(description__contains = q) | Q(name__contains=q))
        context = {"query": q, "rooms" : rooms}
        return render(request, "base/search.html", context)

def room(request, id):
    room =  Room.objects.get(id = id)
    context = {"room" : room}
    return render(request, "base/room.html", context)

# def home(request):
#     rooms = Room.objects.all()
#     context = {"rooms" : rooms}
#     return render(request, "base/home.html", context)





