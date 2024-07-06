from django import forms
from .models import A_User

class UserForm(forms.ModelForm):
    class Meta:
        model=A_User
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control","placeholder":"enter first name"}),
            "age":forms.NumberInput(attrs={"class":"form-control","placeholder":"enter age"}),
            "place":forms.TextInput(attrs={"class":"form-control","placeholder":"enter place"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter email"}),
        }

