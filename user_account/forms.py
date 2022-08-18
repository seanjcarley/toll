from re import M
from django import forms
from .models import UserProfile, UserVehicle

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
            'post_code': 'Postcode'
        }

        self.fields['street1'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholder[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = ''
            self.fields[field].label = False


class UserVehicleForm(forms.ModelForm):
    class Meta:
        model = UserVehicle
        exclude = ('vehicle_id', 'make', 'model', 'color', 'lpn_class',
            'date_added', 'date_removed', 'update_date')

    def __init__(self, *args, **kwargs):
        ''' add place holders and classes, remove auto-generated labels and
        set auto-focus '''
        super.__init__(*args, **kwargs)
        placeholders = {
            'lpn': 'Vehicle Licence Plate Number'
        }
        placeholder = f'{placeholders["lpn"]} *'
        self.fields['lpn'].widget.attrs['placeholder'] = placeholder
        self.fields['lpn'].widget.attrs['autofocus'] = True
        self.fields['lpn'].widget.attrs['class'] = ''
        self.fields['lpn'].widget.label = False


