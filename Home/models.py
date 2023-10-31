from django.db import models
import random
from decimal import Decimal


class Contact(models.Model):
    name=models.CharField( max_length=122)
    email=models.CharField( max_length=122)
    phone=models.CharField( max_length=12)
    description=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name

class PersonalBankingForm(models.Model):
    accountNumber=models.CharField(max_length=12)
    accountName=models.CharField(max_length=122)
    applicantName=models.CharField(max_length=122)
    communicationAddress=models.CharField(max_length=122)
    cellPhoneNo=models.CharField(max_length=12)
    emailAddress=models.CharField(max_length=122)
    date=models.DateField()

    def __str__(self):
        return self.accountNumber 

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    phone_authorised_to_mobile_banking=models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    re_password = models.CharField(max_length=100)
    account_number = models.IntegerField(unique=True, null=True, blank=True)

    def __str__(self):
        return "UserName: " + self.user_name + " Email: " + self.email_address
    
    #def generate_account_number(self):
        #return random.randint(1000000000, 9999999999)
    
    #def save(self, *args, **kwargs):
        #if not self.account_number:
           # self.account_number = self.generate_account_number()
       # super(Customer, self).save(*args, **kwargs)


class Account(models.Model):
    account_id = models.IntegerField()
    phone_authorised_to_mobile_banking = models.CharField(max_length=11,default="NULL")
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Account ID: {self.account_id}, Balance: {self.balance}"

class Bkash(models.Model):
    phone_authorised_to_mobile_banking = models.CharField(max_length=11,default="NULL")
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Account ID: {self.phone_authorised_to_mobile_banking}, Balance: {self.balance}"
