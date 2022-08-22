from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm


# Create your views here.
@login_required
def show_user_profile(request):
    ''' show user profile '''
    profile = get_object_or_404(User, username=request.user)
    print(profile.email)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
        else:
            messages.error(
                request, 'Update failed! Please enter all required details.'
            )
    else:
        form = UserProfileForm(instance=profile)

    template = 'user_account/profile.html'

    context = {
        'form': form,
    }

    return render(request, template, context)
