from django.shortcuts import render,redirect
from .forms import CustomUserCreation
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomeUser, Profile
from .forms import AuthenticationForm, CustomUserProfile


def Login(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'GET':
        form = AuthenticationForm()
        return render(request,'registration/login.html', context={'form': form})
    elif request.method == 'POST':
            pelake_mashin = request.POST.get('pelake_mashin')
            password = request.POST.get('password')      
            user = authenticate(pelake_mashin=pelake_mashin, password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, 'Your pelake_mashin or Password is not valid')
                return redirect(request.path_info)

@login_required
def Logout(request):
    logout(request)
    return redirect('/')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'GET':
        form = CustomUserCreation()
        return render(request,'registration/signup.html', context={'form': form})
    else:
            form = CustomUserCreation(request.POST)
            if form.is_valid():
                form.save()
                pelake_mashin = request.POST.get('pelake_mashin')
                password = request.POST.get('password1')
                user=authenticate(pelake_mashin=pelake_mashin,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('accounts:complate_profile')
                else:
                    messages.add_message(request, messages.ERROR, 'Your pelake_mashin or Password is not valid')
                    return redirect(request.path_info)
            else:
                messages.add_message(request, messages.ERROR, 'Your pelake_mashin or Password is not valid')
                return redirect(request.path_info)            
        
def complate_profile(request):
    if request.method == 'GET':
        #form = CustomUserProfile()
        return render(request,'registration/profile.html')
    elif request.method == 'POST':
        user = Profile.objects.get(user=request.user)
        print (user, request.POST, request.FILES, sep='\n')
        form = CustomUserProfile(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect('/')