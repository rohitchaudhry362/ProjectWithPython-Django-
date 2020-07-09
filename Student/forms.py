from django import forms
from django.forms import ModelForm
from Student.models import Documents
from users.models import MyUser,Student

class DocForm(forms.ModelForm):

    class Meta:
        model = Documents
        fields = '__all__'

class UpdateDocForm(forms.ModelForm):
    class Meta:
        model=Documents
        exclude=('enroll',)

class MyUserForm(forms.ModelForm):
    class Meta:
        model=MyUser
        fields=('first_name','last_name','email','phone_number','userimg',)


class MyUserForm1(forms.ModelForm):
    class Meta:
        model=MyUser
        fields=('first_name','last_name','email','phone_number','userimg',)

class StudentForm1(forms.ModelForm):
    class Meta:
        model=Student
        fields=('sem',)
