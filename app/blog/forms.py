from django import forms

from app.blog.models import Post


class PostFroms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'created_at']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'created_at':forms.DateTimeInput(attrs={
                'class':'form-control',
                
            })
        }