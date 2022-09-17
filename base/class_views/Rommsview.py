from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView

from base.models import Room

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
