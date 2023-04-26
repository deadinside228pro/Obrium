from django import forms

class RegForm(forms.Form):
    login = forms.CharField(label='Логин', required=False, widget=forms.TextInput(attrs={'class': 'mar', 'autocomplete': 'on', 'id': 'login', 'oninput': 'checkParams()'}))
    password = forms.CharField(label='Пароль', widget=(forms.PasswordInput(attrs={'class': 'mar', 'autocomplete': 'on', 'id': 'password', 'oninput': 'checkParams()'})))
    spec_id = forms.IntegerField(label='Спец id', required=False, widget=forms.TextInput(attrs={'class': 'mar', 'autocomplete': 'on', 'id': 'specid', 'placeholder': ' для учителей'}))
