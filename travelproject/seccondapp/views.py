from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid user")
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        one = request.POST['username']
        two = request.POST['first_name']
        three = request.POST['last_name']
        four = request.POST['email']
        five = request.POST['password']
        six = request.POST['password1']
        if five == six:
            if User.objects.filter(username=one).exists():
                print("This username already exist")
                return redirect('register')
            elif User.objects.filter(email=four).exists():
                messages.info(request, "This email already exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username=one, password=five, email=four, first_name=two,
                                                last_name=three)
                user.save()
                return redirect('login')

        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
