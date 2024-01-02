from django import forms
from . models import *
from django.core.validators import RegexValidator

class Lowercase(forms.CharField):
    def to_python(self, value):
        return value.lower()
    
class Uppercase(forms.CharField):
    def to_python(self, value):
        return value.upper()

class ProfileCreateForm(forms.ModelForm):
    #VALIDATION
    # business_name = forms.CharField(
    #     label='Company name',min_length=3, max_length=30,
    #     widget=forms.TextInput(attrs={
    #         'style':'font-size: 14px',
    #         'placeholder': 'Company name'
    #     })
    # )

    # registration_number = forms.CharField(
    #     label='Registration No',  max_length=18,
    #     validators=[RegexValidator(r'^[0-9]*$',
    #     message="Only numbers is allowed!!")],
    #     widget=forms.TextInput(attrs={
    #         'style':'font-size: 14px',
    #         'placeholder': 'Registration no'
    #     })
    # )

    # employee_count = forms.CharField(
    #     label='No of Employees',  max_length=4,
    #     validators=[RegexValidator(r'^[0-9]*$',
    #     message="Only numbers is allowed!!")],
    #     widget=forms.TextInput(attrs={
    #         'style':'font-size: 14px',
    #         'placeholder': 'Total Employees'
    #     })
    # )

    # tax_number = forms.CharField(
    #     label='Tax Identification No',  max_length=18,
    #     validators=[RegexValidator(r'^[0-9]*$',
    #     message="Only numbers is allowed!!")],
    #     widget=forms.TextInput(attrs={
    #         'style':'font-size: 14px',
    #         'placeholder': 'Tax no'
    #     })
    # )


    # address = forms.CharField(
    #     label='Company address',min_length=3, max_length=30,
    #     widget=forms.Textarea(attrs={
    #         'style':'font-size: 14px',
    #         'placeholder': 'Company address',
    #         'rows':5
    #     })
    # )

    # telephone = forms.CharField(
    #     label='Telephone', min_length=8, max_length=50,
    #     validators=[RegexValidator(r'^[0-9]*$',
    #     message="Only numbers is allowed!!")],
    #     widget=forms.TextInput(attrs={
    #         'style':'font-size: 14px',
    #         'placeholder': 'Telephone'
    #     })
    # )

    # mobile = forms.CharField(
    #     label='Mobile',min_length=10, max_length=12,
    #     validators=[RegexValidator(r'^[0-9]*$',
    #     message="Only numbers is allowed!!")],
    #     widget=forms.TextInput(attrs={
    #         'style':'font-size: 14px',
    #         'placeholder': 'Mobile'
    #     })
    # )

    # email = Lowercase(
    #     label='Email', max_length=12,
    #     validators=[RegexValidator(
    #     r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',
    #     message="Put a valid email address")],
    #     widget=forms.TextInput(attrs={
    #         'style':'font-size: 14px',
    #         'placeholder': 'Email'
    #     })
    # )

    # website = forms.CharField(
    #     label='Website', max_length=12,
    #     validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]',
    #     message="Put a valid email address")],
    #     widget=forms.TextInput(attrs={
    #         'style':'font-size: 14px',
    #         'placeholder': 'Website'
    #     })
    # )

    # logo = forms.FileField(
    #     label='Logo', 
    #     required=True,
    #     widget=forms.ClearableFileInput(
    #         attrs={
    #         'style':'font-size: 13px',
    #         'placeholder': 'Company logo'
    #         }
    #     )
    # )



    class Meta:
        model = Profile
        # fields = '__all__'
        # fields = ['item','description','quantity','unit_price']
        expect = ['is_admin']
        #Outside Widgets
        widgets={
   
            'gender': forms.Select(
            attrs={
            'class': 'form-control',
            'style':'font-size: 14px',
            'placeholder': 'Business type'
            })
        }