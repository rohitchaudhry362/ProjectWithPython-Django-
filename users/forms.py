from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from users.models import UserProfile,MyUser,Student,mobile


class MyUserForm(forms.ModelForm):
    phone_number = forms.RegexField(regex=r'^((\+){1}91){1}[1-9]{1}[0-9]{9}$')
    #uniqueid=forms.IntegerField(uniqueid==111111111111 or uniqueid==222222222222 or uniqueid==333333333333 or uniqueid==444444444444)

    class Meta:
        model=MyUser
        fields="__all__"

class UserProfileForm(forms.ModelForm):
    DOB = forms.DateField(required=False, input_formats=['%Y-%m-%d','%m/%d/%Y','%m/%d/%y'] )
    class Meta:
        model=UserProfile
        fields=(
        'userdata',
        'Roleid',
        'DOB',
        'userimg'
        )

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        exclude=('balance',)
class MobileForm(forms.ModelForm):
    mobilenumber = forms.RegexField(regex=r'^((\+){1}91){1}[1-9]{1}[0-9]{9}$')
    class Meta:
        model=mobile
        fields=('mobilenumber',)
