
from django.shortcuts import render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None :
            auth.login(request,user)
            return redirect('button')
        else:
            messages.info(request,'invalid crendentials')
            return redirect('login')
    return render(request,('login.html'))
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        # firstname = request.POST['first_name']
        # lastname = request.POST['last_name']
        # email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('register')
            # elif User.objects.filter(email=email).exists():
            #     messages.info(request,"email already taken")
            #     return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                # print("user registered")
                user.save();
                return redirect('login')

        else:
            messages.info(request,'password not matching')
            return redirect('register')
        return redirect('/')

    return render(request,('register.html'))
def details(request):
    return render(request,'details.html')
def button(request):
    return render(request,'button.html')
def details1(request):
    message = "Order Confirmed"
    return render(request, 'submit.html', {'message': message})