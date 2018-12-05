from django import forms


class ImageUploadForm(forms.Form):
    """Image upload form."""
    file = forms.ImageField()
    title = forms.CharField()