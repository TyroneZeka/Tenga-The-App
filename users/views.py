from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from .forms import CustomUserCreationForm

# Create your views here.
def signup(request):
    page = 'signup'
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request,"User Account Created!")

            login(request,user)
            return redirect('404')


    return render(request,'users/signup.html',{'form':form})

def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect(request.GET['next'] if 'next' in request.GET else '404')

    if request.method == "POST":
        # TODO: implement for both username and email for login
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'Username does not exist!')

        user = authenticate(request,username=username,password= password)
        if user is not None:
            login(request,user)
            return redirect(request.GET['next'] if 'next' in request.GET else '404')
        else:
            messages.error(request,'Username OR password is incorrect')
        
    return render(request,'users/login.html',{})

@login_required(login_url = 'login')
def logoutUser(request):
    logout(request)
    messages.success(request,'User was successfully Logged Out!')
    return redirect('login')

def _404(request):
    return render(request,'404.html',{})

@login_required(login_url='login')
def updateProfile(request):
    context = {}

    return render(request,'users/my-account.html',context)


def cart(request):
    context = {}
    return render(request,'users/cart.html',context)