from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):

    class Meta:

        model = Ticket

        fields = [
            'title',
            'description',
            'category'
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5
            }),

            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
        }