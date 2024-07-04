from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Your email'})
    )
    description = forms.CharField(
        label='Description',
        max_length=1000,
        widget=forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Description'})
    )
