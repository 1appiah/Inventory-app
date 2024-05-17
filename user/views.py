from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import RegistForm, UpdateProfileForm, UpdateUserForm
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}, Continue to log in')
            return redirect('user-login')
    else:    
        form = RegistForm()

    context = {
        'form':form
    }
    return render(request, 'user/register.html',context)

def profile(request):
    return render(request,'user/profile.html')


def profile_update(request):
    if request.method == 'POST':
        form1 = UpdateUserForm(request.POST, instance=request.user)
        form2 = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form1.is_valid() and  form2.is_valid():
            form1.save()
            form2.save()
            return redirect('user-profile')
    else:
        form1 = UpdateUserForm(instance=request.user)
        form2 = UpdateProfileForm(instance=request.user.profile)
    context = {
            'form1': form1,
            'form2': form2
        }    
    return render(request,'user/profile_update.html',context)