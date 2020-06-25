from .models import Comment, Newsletter
from django import forms

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('name', 'body')

    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control'}),
      'body': forms.Textarea(attrs={'class': 'form-control'})
    }

class NewsletterForm(forms.ModelForm):
  class Meta:
    model = Newsletter
    fields = ('email', )