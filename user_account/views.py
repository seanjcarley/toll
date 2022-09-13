from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm, CreateUserForm, UserVehicleForm


# Create your views here.
@login_required
def show_user_profile(request):
    ''' show user profile and allow to update selected details '''
    profile1 = get_object_or_404(UserProfile, user=request.user)
    profile2 = get_object_or_404(User, username=request.user)

    fname = profile2.first_name
    sname = profile2.last_name
    uemail =profile2.email
    uname = profile2.username
    uphone = profile1.phone

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile1)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
        else:
            messages.error(
                request, 'Update failed! Please enter all required details.'
            )
    else:
        form = UserProfileForm(instance=profile1)

    template = 'user_account/profile.html'

    context = {
        'form': form,
        'uname': uname,
        'fname': fname,
        'sname': sname,
        'uemail': uemail,
        'uphone': uphone,
    }

    return render(request, template, context)


def create_user_profile(request):
    ''' create a new user '''
    # profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = CreateUserForm()
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
        else:
            messages.error(request, 'Registration failed!')
    else:
        form1 = CreateUserForm()
        form2 = UserVehicleForm

    template = 'user_account/signup.html'

    context = {
        'form1': form1,
        'form2': form2
    }

    return render(request, template, context)
