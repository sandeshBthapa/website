from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    if request.method == 'POST':
        # Get values

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check password
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'user name already exist')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email already taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, first_name=first_name, email=email,
                                                    last_name=last_name,
                                                    password=password)
                    user.save()
                    messages.success(request, 'you can now login')
                    return redirect('login')


        else:
            messages.error(request, 'password donot match')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you are now login')
            return redirect('dasboard')
        else:
            messages.error(request, 'invalid password or usernae')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
