from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=63)
    first_name = forms.CharField(max_length=63)
    last_name = forms.CharField(max_length=63)
    email = forms.EmailField()
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)
    confirmation_password = forms.CharField(max_length=63, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirmation_password = cleaned_data.get('confirmation_password')
        if password != confirmation_password:
            raise forms.ValidationError('As senhas não são iguais')
        return cleaned_data
