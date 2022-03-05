from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

User = get_user_model()


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='email')

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2',
                  'first_name', 'last_name', 'email']
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия',
                  'email': 'Email', 'password1': 'Пароль',
                  'password2': 'Подтверждение пароля'}

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if not (first_name or last_name):
            raise forms.ValidationError('One of the first name or last name fields must be filled in')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name","last_name", "email")
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Email'}
