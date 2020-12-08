from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import App_users


class CustomUserCreationForm(forms.ModelForm):

	password = 	forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'text_field'}))
	password_rep = 	forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'text_field'}))
	
	class Meta:
    	
		model = App_users
		fields = ('email', 'name', 'role',)
		labels = {
			'name': 'ФИО',
			'role': 'Должность'
		}


	def __init__(self, *args, **kwargs):
		super().__init__(*args,**kwargs)
		self.fields['email'].widget.attrs.update({'class':'text_field'})
		self.fields['name'].widget.attrs.update({'class':'text_field'})
		self.fields['role'].widget.attrs.update({'class':'text_field'})

	def  clean_password_rep(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password_rep']:
			raise forms.ValidationError('пароли не совпадают')
		return cd['password_rep']


class LoginForm(forms.Form):
	email = forms.CharField(widget=forms.EmailInput(attrs={'class':'text_field'}))
	password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'text_field'}))

