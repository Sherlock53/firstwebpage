from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Post, Comment
from django.contrib.auth.models import User

class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class PostForm(BaseForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(BaseForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


class UserForm(BaseForm):
    class Meta:
        model = User
        fields = ('username',  'password')

class UserRegForm(BaseForm):

    class Meta:
        model = User
        fields=('username','password')
        widgets = {
            'username': forms.TextInput(
                attrs={ 'placeholder': 'Username', 'id': 'username'}),
            'password': forms.PasswordInput(
                    attrs={
                        'placeholder': 'Password',
                        'id': 'password',
                    }),
        }
