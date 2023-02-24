from apis.models import *
from django import forms
from django.forms.widgets import (CheckboxInput, EmailInput, FileInput,
                                  NumberInput, RadioSelect, Select,
                                  SelectMultiple, Textarea, TextInput,
                                  URLInput)
from django.utils.translation import ugettext_lazy as _


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ("timestamp",)
        widgets = {
            "name": TextInput(
                attrs={
                    "class": "required form-control",
                    "id": "name",
                    "placeholder": "Name",
                }
            ),
            "title": TextInput(
                attrs={
                    "class": "required form-control",
                    "id": "title",
                    "placeholder": "Title",
                }
            ),
            "description": TextInput(
                attrs={
                    "class": "required form-control",
                    "id": "description",
                    "placeholder": "Description",
                }
            ),
        }
