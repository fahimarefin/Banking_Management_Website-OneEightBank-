from django.contrib import admin
from Home.models import Contact
from Home.models import PersonalBankingForm
from Home.models import Customer
from Home.models import Account
from Home.models import Bkash
# Register your models here.
admin.site.register(Contact)
admin.site.register(PersonalBankingForm)
admin.site.register(Customer)
admin.site.register(Account)
admin.site.register(Bkash)

