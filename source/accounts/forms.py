from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if not first_name and not last_name:
            raise forms.ValidationError('Хотя бы одно из полей (Имя, Фамилия) должно быть заполнено!')

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Электронная почта'
        }
