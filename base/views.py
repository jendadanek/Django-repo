from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
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



