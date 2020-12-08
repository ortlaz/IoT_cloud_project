from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
# from .models import App_users

# Create your views here.
def index(request):
	return render(
		request,
		'index.html'
	)

def singup_done(request):
	return render(
		request,
		'singup_done.html'
	)

def error(request):
	return render(
		request,
		'error.html'
	)

def singin(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(email=cd['email'], password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('controlPanel')
				else:
					return redirect('error')
			else:
			 	messages.error(request, 'Неверное имя пользователя или пароль')
			 	return render(request, 'singin.html', {'form': form})
	else:
		form = LoginForm()

	return render(request, 'singin.html', {'form': form})

def singup(request):
	if request.method == 'POST':
		user_form = CustomUserCreationForm(request.POST)
		if user_form.is_valid():
			new_user = user_form.save(commit=False)
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			return redirect('singup_done')
	else:
		user_form = CustomUserCreationForm()

	return render(request,'singup.html',{'user_form': user_form})

@login_required
def control_panel(request):
	cur_user = request.user

	ids = []

	for i in range(10):
		ids.append(i)


	context = {
		'cur_user':cur_user,
		'ids': ids,

	}
	return render(request, 'controlPanel.html', context=context)


	