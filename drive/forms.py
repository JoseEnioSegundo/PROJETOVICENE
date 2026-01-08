from django import forms
from .models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["title", "image"]

        labels = {
            "title": "Título",
            "image": "Imagem",
        }

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Título (opcional)"
            }),
            "image": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),
        }
