from users.models import Student
from django import forms
from django.forms import ModelForm


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=('balance',)
