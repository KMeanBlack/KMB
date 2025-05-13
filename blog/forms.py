from django import forms
from .models import Post

from ckeditor.fields import RichTextField


class TextForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, required=True)

class AddBlogForm(forms.ModelForm):
    description = RichTextField()
    
    class Meta:
        model = Post
        fields = (
            "title",
            "category",
            "content",
            "image"
        )