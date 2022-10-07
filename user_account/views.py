import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from .models import UserProfile, UserVehicle
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

    template = 'user_account/profile.html'

    return render(request, template, context)


@login_required
def show_vehicles(request):
    ''' show the vehicles on the account and allow new vehicles to be added '''
    profile1 = get_object_or_404(UserProfile, user=request.user)
    profile2 = get_object_or_404(User, username=request.user)
    fname = profile2.first_name
    vehicles = UserVehicle.objects.filter(
        account__account_no=profile1.account_no)
    
    if request.method == 'POST':
        try:
            vehicle = VehicleDetails.objects.get(lpn=request.POST['lpn'])
            form2_data = {
                'lpn': request.POST['lpn'],
                'make': vehicle.make,
                'model': vehicle.model,
                'color': vehicle.color,
                'lpn_class': vehicle.lpn_class,
            }

            form2 = UserVehicleForm(form2_data)

            if form2.is_valid():
                vehiclef = form2.save(commit=False)
                vehiclef.account = profile1.account_no
                vehiclef.vehicle_id = VehicleDetails.objects.get(
                    lpn = request.POST['lpn'])
                vehiclef.save()
                messages.success(request, 'Vehicle Successfully Added!')
                return redirect('vehicles')

        except VehicleDetails.DoesNotExist:
            messages.error(request, 'The vehicle {} does not exist in the \
                vehicle database!'.format(request.POST['lpn']))
            form2 = UserVehicleForm()
    else:
        form2 = UserVehicleForm()

    context = {
        'fname': fname,
        'vehicles': vehicles,
        'form2': form2,
    }

    template = 'user_account/vehicle_details.html'

    return render(request, template, context)


def create_user_profile(request):
    ''' create a new user '''
    if request.method == 'POST':
        try:
            vehicle = VehicleDetails.objects.get(lpn=request.POST['lpn'])
            form2_data = {
                'lpn': request.POST['lpn'],
                'make': vehicle.make,
                'model': vehicle.model,
                'color': vehicle.color,
                'lpn_class': vehicle.lpn_class,
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
                vehiclef = form2.save(commit=False)
                contact = form3.save(commit=False)
                contact.account_no = account_no
                form1.save()
                contact.user = User.objects.get(
                    username = request.POST['username'])
                contact.save()
                vehiclef.account = UserProfile.objects.get(user = contact.user)
                vehiclef.vehicle_id = VehicleDetails.objects.get(
                    lpn = request.POST['lpn'])
                vehiclef.save()
                login(request, contact.user)
                messages.success(request, 'Registration successful!')
                return redirect('profile')
            else:
                messages.error(request, 'Registration failed!')
        except VehicleDetails.DoesNotExist:
            messages.error(request, 'The vehicle {} does not exist in the \
                vehicle database!'.format(request.POST['lpn']))
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
    if is_ajax(request=request) and request.method == 'GET':
        try:
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
            instance = json.dumps(formv_data)
            return JsonResponse({"instance": instance}, status=200)
        except VehicleDetails.DoesNotExist:
            messages.error(
                request, 'The vehicle {} does not exist in the vehicle database!'.format(request.GET.get('lpn')))
            return JsonResponse({"error": True}, status=400)


def create_acc_no():
    num = User.objects.aggregate(Max('id'))
    return num['id__max'] + 10


def check_user_name(request):
    if is_ajax(request=request) and request.method == 'GET':
        uname = request.GET.get('username', None)
        print(uname)
        if User.objects.filter(username = uname).exists():
            return JsonResponse({"valid": False}, status=200)
        else:
            return JsonResponse({"valid": True}, status=200)
    return JsonResponse({}, status = 400)

def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH") == 'XMLHttpRequest'
