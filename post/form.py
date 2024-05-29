from django import forms
from .models import Posts

class PostsForm(forms.ModelForm):
    content_posts = forms.CharField(max_length=400, label="Crear nueva publicación",required=True, widget= forms.Textarea(attrs={"class":"form-control"}))
    img = forms.ImageField(label="Seleccionar imagen", required=False,widget= forms.FileInput(attrs={"class":"form-control-file", }))
    class Meta:
        model = Posts
        fields = ['content_posts', 'img']