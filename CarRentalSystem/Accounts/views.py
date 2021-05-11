from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages


# Create your views here.
def Register(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['uname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                # return render(request,'register.html',{'message':'username exist'})
                messages.info(request, 'Username exists')
                return redirect('Register')
            elif User.objects.filter(email=email).exists():
                # return render(request, 'register.html', {'message': 'email exist'})
                messages.info(request, 'email exists')
                return redirect('Register')
            else:
                user = User.objects.create_user(username=username, password=password1, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save()
                return redirect('login')
        else:
            # return render(request, 'register.html', {'message': 'password mismatch'})
            messages.info(request, 'password doesnt match')
            return redirect('Register')
    else:
        return render(request, 'Register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_superuser:
                messages.info(request, 'this is a admin account')
                return redirect('login')
            else:
                auth.login(request, user)
                return redirect('/')
        else:
            messages.info(request, 'invalid username or password')
            return redirect('login')
    else:
        return render(request, 'Login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def silver(request):
    user = auth.get_user(request)
    if user.username:
        return redirect('Booking')
    else:
        return render(request, 'login.html')
