from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Логин или Email', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))



class MyUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = None
            field.widget.attrs['class'] = 'form-control'

    avatar = forms.ImageField(required=True,widget=forms.FileInput(),label="Аватар")
    email = forms.EmailField(required=True,widget=forms.EmailInput(),label="Email")
    phone_number = forms.CharField(
        required = False,
        label='Телефон',
        widget=forms.TextInput(attrs={
            'placeholder': '+996 700 000 000',
            'type': 'tel',
        })
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username' , 'email', 'password1', 'password2', 'avatar', 'first_name', 'bio', 'phone_number','gender']