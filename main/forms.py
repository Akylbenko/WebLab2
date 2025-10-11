from django.forms import ModelForm, TextInput, Textarea
from .models import Feedbacks

class FeedbacksForm(ModelForm):
    class Meta:
        model = Feedbacks
        fields = ['name', 'email','content']
        widgets = {
            "name": TextInput(attrs={'class':'form-control', 'placeholder':'Имя'}),
            "email": TextInput(attrs={'class':'form-control', 'placeholder':'Почта'}),
            "content": Textarea(attrs={'class':'form-control', 'placeholder':'Комментарий'}),
        }
