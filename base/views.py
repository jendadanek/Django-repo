from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views1 here.
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView

from base.forms import RoomForm
from base.models import Room, Message


def hello(request):
    s = request.GET.get('s', ' ')
    return HttpResponse(f"Hello {s}")



@login_required
@permission_required(['base.view_room', 'base.view_message'])
def search(request):
    """  Hledání  v url adrese """
    q = request.GET.get('q', ' ')
    if q == ' ' :
            return HttpResponse("Zadejte co chcete hledat")
    else:
        rooms = Room.objects.filter(Q(description__contains = q) | Q(name__contains=q))
        context = {"query": q, "rooms" : rooms}
        return render(request, "base/search.html", context)
@login_required
@permission_required(['base.view_room', 'base.view_message'])
def room(request, id):
    """ vytváření zpráv do místnosti """
    room = Room.objects.get(id=id)
    messages = room.message_set.all()

    # POST
    if request.method == 'POST':
        Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', id=room.id)

    # GET
    context = {'room': room, 'messages': messages}
    return render(request, 'base/room.html', context)


# def home(request):
    """  Ukazuje nám seznam místností jako hlavní stránku   """
#     rooms = Room.objects.all()
#     context = {"rooms" : rooms}
#     return render(request, "base/home.html", context)


class RoomDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    template_name = 'base/room_confirm_delete.html'
    model = Room
    success_url = reverse_lazy('rooms')
    permission_required = 'base.delete_room'

class RoomUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    template_name = 'base/room_form.html'
    model = Room
    form_class = RoomForm
    success_url = reverse_lazy('rooms')
    permission_required = 'base.change_room'

    def form_invalid(self, form):
        return super().form_invalid(form)

class RoomCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    template_name = 'base/room_form.html'
    form_class = RoomForm
    success_url = reverse_lazy('rooms')
    permission_required = 'base.add_room'
    def form_invalid(self, form):
        return super().form_invalid(form)

    # class MassageCreateView(CreateView):
    #     #     """ Zjednodušení  RoomCreateView(FormView) """
    #     #     template_name = 'base/room.html'
    #     #     form_class = RoomForm
    #     #     success_url = reverse_lazy('home')
    #     #
    #     #     def form_invalid(self, form):
    #     #         return super().form_invalid(form)



    # class RoomCreateView(FormView):
    """ Zjednodušení room_create(request)  """
#     template_name = 'base/room_form.html'
#     form_class = RoomForm
#     success_url = reverse_lazy('home')
#
#     def form_valid(self, form):
#         result = super().form_valid(form)
#         cleaned_data = form.cleaned_data
#         Room.objects.create(
#             name=cleaned_data['name'],
#             description=cleaned_data['description'],
#         )
#         return result
#
#     def form_invalid(self, form):
#         return super().form_invalid(form)

# def room_create(request):
    """ posílání a vyplnování formulářů pro vytvočení místnosti """
#     if request.method == "GET":
#         form = RoomForm()
#         context = {"form" : form}
#         return render(request, "base/room_form.html", context)
#     elif request.method == "POST":
#         form = RoomForm(request.POST)
#         if form.is_valid():
#             form.save()
#     return redirect("home")


#
# class Roomsview(View):
    """"" vytváří seznam místností """
#      def get(self, request):
#          rooms = Room.objects.all()
#          context = {"rooms": rooms}
#          return render(request, "base/home.html", context)


# class Roomsview(TemplateView):
    """  Zjednodušuje  Roomsview(View) """
#     rooms = Room.objects.all()
#     template_name = "base/home.html"
#     extra_context = {"rooms": rooms}

class Roomsview(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    """  Zjednodušuje Roomsview(TemplateView) """
    template_name = "base/home.html"
    model = Room
    permission_required = 'base.view_room'




