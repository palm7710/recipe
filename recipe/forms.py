from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ["title", "content", "description", "image", "user",]
        widgets = {
            "user": forms.HiddenInput()
        }
