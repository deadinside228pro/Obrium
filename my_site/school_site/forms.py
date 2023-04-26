from django import forms


class RegForm(forms.Form):
    login = forms.CharField(label='Логин', required=False, widget=forms.TextInput(
        attrs={'class': 'mar', 'autocomplete': 'on', 'id': 'login', 'oninput': 'checkParams()'}))
    password = forms.CharField(label='Пароль', widget=(forms.PasswordInput(
        attrs={'class': 'mar', 'autocomplete': 'on', 'id': 'password', 'oninput': 'checkParams()'})))
    teacher_check = forms.BooleanField(label='Войти как учитель', required=False, widget=forms.CheckboxInput(
        attrs={'class': 'mar', 'autocomplete': 'on', 'id': 'specid', 'placeholder': ' для учителей'}))

