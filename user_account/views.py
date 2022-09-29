import json
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core import serializers
from django.http import JsonResponse
from .models import UserProfile
from .forms import UserProfileForm, CreateUserForm, UserVehicleForm
from vehicles.models import VehicleDetails
from django.db.models import Q, Max


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
    if request.method == 'POST':
        try:
            vehicle = VehicleDetails.objects.get(lpn=request)
            form2_data = {
                'lpn': request.POST['lpn'],
                'make': vehicle.make,
                'model': vehicle.model,
                'color': vehicle.color,
                'class': vehicle.lpn_class,
            }
            account_no = create_acc_no()
            form3_data = {
                'street1': request.POST['street1'],
                'street2': request.POST['street2'],
                'street3': request.POST['street3'],
                'town_city': request.POST['town_city'],
                'county': request.POST['county'],
                'post_code':request.POST['post_code'],
                'country': request.POST['country'],
                'phone': request.POST['phone'],
            }

            form1 = CreateUserForm(request.POST)
            form2 = UserVehicleForm(form2_data)
            form3 = UserProfileForm(form3_data)


            if form1.is_valid() and form2.is_valid() and form3.is_valid():
                form1.save(commit=False)
                vehicle = form2.save(commit=False)
                contact = form3.save(commit=False)
                contact.account_no = account_no
                form1.save()
                contact.user = User.objects.get(username = request.POST['username'])
                contact.save()
                vehicle.account = UserProfile.get(user = contact.user)
                vehicle.save()
                login(request, contact.user)
                messages.success(request, 'Registration successful!')
                return redirect('show_user_profile')
            else:
                messages.error(request, 'Registration failed!')
        except VehicleDetails.DoesNotExist:
            messages.error(request, 'The vehicle {} does not exist in the vehicle database!'.format(request.POST['lpn']))
            form1 = CreateUserForm(request.POST)
            form2 = UserVehicleForm()
            form3 = UserProfileForm(request.POST)
    else:
        form1 = CreateUserForm()
        form2 = UserVehicleForm()
        form3 = UserProfileForm()


    template = 'user_account/signup.html'

    context = {
        'form1': form1,
        'form2': form2,
        'form3': form3,
    }

    return render(request, template, context)


def get_vehicle_info(request):
    try:
        if is_ajax(request=request) and request.method == 'GET':
            vrn = request.GET.get('lpn', None)
            vquery = Q(lpn=vrn)
            vehicle = VehicleDetails.objects.get(vquery)
            formv_data = {
                    "lpn": request.GET['lpn'],
                    "make":  vehicle.make,
                    "model": vehicle.model,
                    "color": vehicle.color,
                    "class": vehicle.lpn_class,
                }
            formv = UserVehicleForm(formv_data)

            if formv.is_valid():
                instance = json.dumps(formv_data)
                return JsonResponse({"instance": instance}, status=200)
            else:
                return JsonResponse({"error": formv.errors}, status=400)
        return JsonResponse({"error": ""}, status=400)
    except VehicleDetails.DoesNotExist:
        messages.error(
            request, 'The vehicle {} does not exist in the vehicle database!'.format(request.GET.get('lpn')))


def create_acc_no():
    num = User.objects.aggregate(Max('id'))
    return num['id__max'] + 10


def check_user_name(request):
    if is_ajax(request=request) and request.method == 'GET':
        uname = request.GET.get('username', None)
        print(uname)
        if User.objects.filter(username = uname).exists():
            print(1)
            return JsonResponse({"valid": False}, status=200)
        else:
            print(2)
            return JsonResponse({"valid": True}, status=200)
    print(3)
    return JsonResponse({}, status = 400)

def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH") == 'XMLHttpRequest'
