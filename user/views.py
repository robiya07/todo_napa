from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, UserProfileForm, ImageUploadForm
from .models import UserModel
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.contrib import messages

# Create your views here.
def home_view(request):
    return render(request, "main/home.html")


@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, "main/logout.html")


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                messages.info(request, 'You have successfully logged into your account!')
                return redirect('task_list')
            raise ValidationError('Password or Username is incorrect!', 'password')
    return render(request, 'main/login.html', context={
        'login_form': form
    })


def registration_view(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = UserModel(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                password=make_password(form.cleaned_data['password'])
            )
            user.save()
            return redirect('login')
    return render(request, 'main/registration.html', context={
        'registration_form': form
    })


@login_required
def img_delete(request, id):
    user = UserModel.objects.get(id=id)
    user.user_img = 'icon/user_icon.png'
    user.save()
    return redirect('profile')


@login_required
def img_upload(request):
    if request.method == "POST":
        form = ImageUploadForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            user = UserModel.objects.get(username=request.user)
            user.user_img = form.cleaned_data['user_img']
            user.save()
            return redirect('profile')
    return render(request, 'main/profile.html')


@login_required
def profile_view(request):
    user = UserModel.objects.get(username=request.user)
    if request.method == "POST":
        form = UserProfileForm(data=request.POST)
        if form.is_valid():
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            return redirect('profile')
    return render(request, 'main/profile.html', context={
        'user': user
    })
