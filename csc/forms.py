from django import forms
from .models import Ebooks, Contact


class EbookSearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Search ebooks ...'})
    )


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
