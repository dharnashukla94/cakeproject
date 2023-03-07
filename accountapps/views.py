from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import RegistrationForm


# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = RegistrationForm()
    context = {
        'form': form

    }
    return render(request, 'registration.html', context)

# Login page using html
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')

# Register form using html
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already registered, please enter different email')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, email=email, password=password1,
                                                first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login')

        else:
            messages.info(request, 'Password does not match, please re-enter the password')
            return redirect('register')

    else:
        return render(request, 'register.html')

# logout using html
def logout(request):
    auth.logout(request)
    return redirect('/')
