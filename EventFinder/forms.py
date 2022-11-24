from django import forms
from . import models


class registerForm(forms.ModelForm):
    class Meta:
        model = models.register
        fields = ("first_name", "last_name", "phone_number", "email_address")
        # exclude = ("event")
