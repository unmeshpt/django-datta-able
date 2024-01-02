from django.db import models


# Create your models here.
class BusinessType(models.Model):    
    business_type = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.business_type
    
class Company(models.Model):
    business_name = models.CharField(max_length=30)
    logo = models.FileField(upload_to='files/company_assets/', null=True, blank=True)
    business_type =  models.ForeignKey(BusinessType, on_delete=models.DO_NOTHING, related_name='business_types', verbose_name='BusinessType') # models.CharField(max_length=100)
    tax_number = models.CharField(max_length=20, null=True, blank=True)
    registration_number = models.CharField(max_length=50, null=True, blank=True)
    license_number = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    telephone = models.CharField(max_length=12, null=True, blank=True)
    mobile = models.CharField(max_length=12, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    founded_on = models.DateField(null=True, blank=True)
    company_mission = models.TextField(null=True, blank=True)
    company_vision = models.TextField(null=True, blank=True)
    company_values = models.TextField(null=True, blank=True)
    terms_and_conditions = models.TextField(null=True, blank=True)
    business_description = models.TextField(null=True, blank=True)
    partnerships_affiliations = models.TextField(null=True, blank=True)
    employee_count = models.IntegerField(null=True, blank=True)
    legal_contacts = models.TextField(null=True, blank=True)
    emergency_contacts = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.business_name
    
class CurrencyPreferences(models.Model):
    CURRENCY_CHOICES = [
        ('usd', 'USD - United States Dollar'),
        ('eur', 'EUR - Euro'),
        ('gbp', 'GBP - British Pound'),
        ('inr', 'INR - Indian Rupee'),
        ('qar', 'QAR - Qatar Riyal'),
        # Add more currency choices as needed
    ]

    company = models.OneToOneField('Company', on_delete=models.CASCADE, related_name='currency_preferences')
    preferred_currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, verbose_name='Preferred Currency')

    # Additional fields based on your requirements
    conversion_rate = models.DecimalField(max_digits=10, decimal_places=6, verbose_name='Conversion Rate')

    # Add more fields as needed

    def __str__(self):
        return f'{self.user.username} - {self.get_preferred_currency_display()}'

    class Meta:
        verbose_name = 'Currency Preferences'
        verbose_name_plural = 'Currency Preferences'

class InsuranceInformation(models.Model):
    # Fields for basic insurance information
    policy_number = models.CharField(max_length=50, verbose_name='Policy Number')
    provider_name = models.CharField(max_length=100, verbose_name='Insurance Provider')
    start_date = models.DateField(verbose_name='Coverage Start Date')
    end_date = models.DateField(verbose_name='Coverage End Date')
    
    # Additional fields based on your requirements
    insured_person_name = models.CharField(max_length=100, verbose_name='Insured Person Name')
    coverage_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Coverage Amount')

    # Add more fields as needed

    def __str__(self):
        return f'{self.policy_number} - {self.provider_name}'

    class Meta:
        verbose_name = 'Insurance Information'
        verbose_name_plural = 'Insurance Information'

class BankAccount(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='bank_details')
    account_number = models.CharField(max_length=20)
    account_holder_name = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255)
    branch_name = models.CharField(max_length=255)
    ifsc_code = models.CharField(max_length=20)
    upi_number = models.CharField(max_length=13,null=True,  blank=True)
    upi_id = models.CharField(max_length=25, null=True,  blank=True)
    primary=models.BooleanField()

    def __str__(self):
        return f"Bank Account for {self.company.business_name}"

class PricingStructure(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='price_structure')
    pricing_name = models.CharField(max_length=255)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.company.business_name} - {self.pricing_name}"

class OwnershipInformation(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='ownership_details')
    owner_name = models.CharField(max_length=255)
    ownership_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)

    def __str__(self):
        return f"Ownership Information for {self.company.business_name}"

class ClientTestimonial(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='client_testimonial')
    client_name = models.CharField(max_length=255)
    testimonial_text = models.TextField()

    def __str__(self):
        return f"Testimonial for {self.company.business_name} by {self.client_name}"

    
class SocialMediaProfile(models.Model):
    SOCIAL_MEDIA_CHOICES = [
        ('facebook', 'Facebook'),
        ('x', 'X'),
        ('instagram', 'Instagram'),
        ('snapchat', 'Snapchat'),
        ('tiktok', 'Tiktok'),
        # Add more social media platforms as needed
    ]
    company =  models.ForeignKey(Company, on_delete=models.CASCADE, related_name='socialmedia')
    profile_name = models.CharField(max_length=100, verbose_name='Profile Name')
    platform = models.CharField(max_length=20, choices=SOCIAL_MEDIA_CHOICES, verbose_name='Social Media Platform')
    profile_url = models.URLField(verbose_name='Profile URL')

    # Additional fields based on your requirements
    followers_count = models.IntegerField(verbose_name='Followers Count')
    date_joined = models.DateField(verbose_name='Date Joined')

    # Add more fields as needed

    def __str__(self):
        return f'{self.profile_name} - {self.get_platform_display()}'

    class Meta:
        verbose_name = 'Social Media Profile'
        verbose_name_plural = 'Social Media Profiles'


class Services(models.Model):
    company =  models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_services')
    service=models.CharField(max_length=100,  unique=True)
    description=models.TextField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f"{self.service}"

class Products(models.Model):
    services =  models.ForeignKey(Services, on_delete=models.CASCADE, related_name='company_products')
    product=models.CharField(max_length=100,  unique=True)
    description=models.TextField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f"{self.product}"