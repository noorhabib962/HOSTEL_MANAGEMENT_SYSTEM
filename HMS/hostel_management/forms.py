from django import forms
from .models import Hostel
class HostelForm(forms.ModelForm):
    class Meta:
        model = Hostel
        fields = ('name','email','phone','capacity','address')
        widgets = { 
            'name': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Username' }), 
            'email': forms.EmailInput(attrs={ 'class': 'form-control', 'placeholder': 'Email' }),
            'phone': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Phone' }), 
            'capacity': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Capacity' }),
            'address': forms.Textarea(attrs={ 'class': 'form-control', 'placeholder': 'Address' }),
        
            } 