from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views1 here.
from django.views.generic import ListView

from base.forms import RoomForm
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


def room_create(request):
    if request.method == "GET":
        form = RoomForm()
        context = {"form" : form}
        return render(request, "base/room_form.html", context)
    elif request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")


#
# class Roomsview(View):
#      def get(self, request):
#          rooms = Room.objects.all()
#          context = {"rooms": rooms}
#          return render(request, "base/home.html", context)


# class Roomsview(TemplateView):
#     rooms = Room.objects.all()
#     template_name = "base/home.html"
#     extra_context = {"rooms": rooms}

class Roomsview(ListView):
    template_name = "base/home.html"
    model = Room



