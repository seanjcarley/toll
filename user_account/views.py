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

    user = profile.username     

    template = 'user_account/profile.html'

    context = {
        'user': user
    }

    print(user)
    print(template)

    return render(request, template, context)
