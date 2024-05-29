from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    content = forms.CharField(max_length=200, label="Comentario", required=True, widget=forms.TextInput(attrs={'class':'form-control', "placeholder":"Agregar comentario"}))
    class Meta:
        model = Comment
        fields = ['content']
        
        widgets = {
            'posts': forms.HiddenInput()  # Campo oculto para almacenar el ID de la publicación
        }