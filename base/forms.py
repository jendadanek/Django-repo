from django.core.exceptions import ValidationError
from django.forms import ModelForm

from base.models import Room

import logging


class RoomForm(ModelForm):

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 2:
            validation_error = ValidationError("Name must contains minimal 2 chars.")
            logging.warning(f"{validation_error}: {name}")
            raise validation_error
        if Room.objects.filter(name__iexact=name).exists():
            validation_error = ValidationError("Name was already created")
            logging.warning(f"{validation_error}: {name}")
            raise validation_error
        return name



    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['participants']


