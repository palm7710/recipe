from django import forms
from comment.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content", "recipe", ]
        widgets = {
            "recipe": forms.HiddenInput()
        }
        labels = {
            "content": "コメントをどうぞ"
        }
