from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, UserVehicle
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'account_no', 'date_added', 
            'date_removed', 'update_date')

    def __init__(self, *args, **kwargs):
        ''' add place holders and classes, remove auto-generated labels and 
        set auto-focus '''
        super().__init__(*args, **kwargs)
        placeholders = {
            'street1': 'Street Address 1',
            'street2': 'Street Address 2',
            'street3': 'Street Address 3',
            'town_city': 'Town or City',
            'county': 'County',
            'post_code': 'Postcode',
            'phone': 'Phone',
        }

        self.fields['street1'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs.update(style='max-width: 20em')
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = ''
            self.fields[field].label = False


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 
                    'password1', 'password2')

    def __init__(self, *args, **kwargs):
        ''' add placeholders and classes, remove auto-generated labels and
        set auto-focus '''
        super().__init__(*args, **kwargs)
        placeholders = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'password1': 'Enter a Password',
            'password2': 'Re-Enter Password',
        }
        # self.fields['username'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs.update(style='max-width: 20em')
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].widget.attrs['class']= ''
        self.fields[field].label = False

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        if commit:
            user.save()
        return User


class UserVehicleForm(forms.ModelForm):
    class Meta:
        model = UserVehicle
        exclude = ('account','vehicle_id', 'date_added', 'date_removed', 
                    'update_date')

    def __init__(self, *args, **kwargs):
        ''' add placeholders and classes, remove auto-generated labels and
        set auto-focus '''
        super().__init__(*args, **kwargs)
        placeholders = {
            'lpn': 'Vehicle Licence Plate Number',
            'make': '', 
            'model': '', 
            'color': '', 
            'lpn_class': '',
        }
        placeholder = f'{placeholders["lpn"]} *'
        for field in self.fields:
            self.fields[field].widget.attrs.update(style='max-width: 20em')
            if field != 'lpn':
                self.fields[field].widget = forms.HiddenInput()
            if field == 'lpn':
                self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].widget.attrs['class']= ''
        self.fields[field].label = False        
