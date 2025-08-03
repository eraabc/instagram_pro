from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import get_user_model, authenticate
from django.db.models import Q
from django.forms import ModelForm

User = get_user_model()

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Логин или Email', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean(self):
        username_or_email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username_or_email and password:
            try:
                user_obj = User.objects.get(Q(username=username_or_email) | Q(email=username_or_email))
                username = user_obj.username
            except User.DoesNotExist:
                username = username_or_email

            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    "Неверный логин, email или пароль."
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


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


class MyUserChangeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = None
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ['username' , 'email', 'avatar', 'first_name', 'bio', 'phone_number','gender']




class StyledPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Старый пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        })
    )
    new_password1 = forms.CharField(
        label='Новый пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        })
    )
    new_password2 = forms.CharField(
        label='Подтвердите новый пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        })
    )