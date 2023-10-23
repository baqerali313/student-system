from django import forms
from .models import Student


class Form1(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'age': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Enter your Age Here : '}),
            'name': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Enter your Name Here : '}),
            'class_st': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Enter your Class Here : '}),
            'city': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Enter your City Here : '}),

        }

