from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from Home.models import Contact
from Home.models import PersonalBankingForm
from Home.models import Account
from Home.models import Bkash
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout,login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Customer
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.db import migrations
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from decimal import Decimal
import random
from django.contrib.auth.decorators import login_required



#def profile(request):
    #user = request.user
   # context = {
        #'user': user,
    #}
   # return render(request, 'profile.html', context)

from django.shortcuts import render
from .models import Customer

def profile(request):
    customer = Customer.objects.get(user_name=request.user.username)
    context = {
        'customer': customer,
    }
    return render(request, 'profile.html', context)



  



# Create your views here.
def index(request):
       return render(request,'index.html')
    #return HttpResponse("this is homepage")
def about(request):
   # return HttpResponse("this is aboutpage")
   return render(request,'about.html')
def services(request):
    #return HttpResponse("this is servicepage")
    return render(request,'services.html')
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        description=request.POST.get('description')
        
        new_contact = Contact(
            name=name,
            email=email,
            phone=phone,
            description=description,
            date=datetime.today()
        )
        new_contact.save()
        messages.success(request, 'You message has been sent!')
    
    return render(request,'contact.html')

def devs(request):
    return render(request,'devs.html')

def portfolioFahim(request):
    return render(request,'portfolioFahim.html')
def portfolioAni(request):
    return render(request,'portfolioAni.html')
def portfolioSumya(request):
    return render(request,'portfolioSumya.html')
def personalBanking(request):
    return render(request,'personalBanking.html')
def index_after_signin(request):
    return render(request,'index_after_signin.html')

def personalBankingForm(request):
    if request.method=='POST':
        accountNumber=request.POST.get('accountNumber')
        accountName=request.POST.get('accountName')
        applicantName=request.POST.get('applicantName')
        communicationAddress=request.POST.get('communicationAddress')
        cellPhoneNo=request.POST.get('cellPhoneNo')
        emailAddress=request.POST.get('emailAddress')
        
        new_personalBankingForm = PersonalBankingForm(
            accountNumber=accountNumber,
            accountName=accountName,
            applicantName=applicantName,
            communicationAddress=communicationAddress,
            cellPhoneNo=cellPhoneNo,
            emailAddress=emailAddress,
            date=datetime.today()
        )
        new_personalBankingForm.save()
        messages.success(request, 'You message has been sent!')
    return render(request,'personalBankingForm.html')
def prepaidcard(request):
    return render(request,'prepaidcard.html')
def debitcard(request):
    return render(request,'debitcard.html')
def signup(request):
    if request.method == "GET":
        return render(request,'signup.html')

    elif request.method =='POST':
        
        first_name= request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        user_name= request.POST.get("user_name")
        email_address= request.POST.get('email_address')
        phone_number= request.POST.get('phone_number')
        phone_authorised_to_mobile_banking=request.POST.get('phone_authorised_to_mobile_banking')
        address=request.POST.get('address')
        city=request.POST.get('city')
        password= request.POST.get('password')
        re_password= request.POST.get('re_password')
        account_number= random.randint(1000000000, 9999999999)
        
        myuser = Customer(
            first_name= first_name,
            last_name=last_name,
            user_name=user_name,
            email_address=email_address,
            phone_number=phone_number,
            phone_authorised_to_mobile_banking=phone_authorised_to_mobile_banking,
            address=address,
            city=city,
            password=password,
            re_password=re_password,
            account_number=account_number
            
            
            
           
        )
        
        print("Phone Number:" ,phone_number)

        if password != re_password:
            return render(request,'signup.html',{'prompt':"Sorry Your Passwords Doesn't Match"})
        if Customer.objects.filter(phone_authorised_to_mobile_banking=phone_authorised_to_mobile_banking).exists():
             return render(request,'signup.html',{'prompt':"Phone Number Already Exists"})

        elif User.objects.filter(username=user_name).exists():
            return render(request,'signup.html',{'prompt':"Username Already Exists"})

        elif User.objects.filter(email=email_address).exists():
            return render(request,'signup.html',{'prompt':"Email Already Exists"})
        

        else:
            myuser = User.objects.create_user(username=user_name,email=email_address,password=password,first_name=first_name,last_name=last_name)
            myuser.save()

            ins =Customer(first_name=first_name,last_name=last_name,user_name=user_name,email_address=email_address,phone_number=phone_number,address=address,city=city,password=password,re_password=re_password,account_number=account_number,
                          phone_authorised_to_mobile_banking=phone_authorised_to_mobile_banking)
            ins.save()

            user = authenticate(username= user_name,password = password)

            if user is not None:
                login(request,user)
                return redirect("index")
            
            else:
                return render(request,'signup.html')

def log_in(request):
    if request.method == "GET":
        return render(request, "log_in.html", {"name": "Customer"})

    elif request.method == "POST":
        username = request.POST["user_name"]
        password = request.POST["password"]
        

        user = authenticate(username= username,password = password)

        if user is not None:
            login(request,user)
            if user.is_staff==True:
                return redirect(reverse('admin:index'))
                #return render(request, "/loc_admin")
            elif user.is_staff==False:
                return render(request, "index_after_signin.html")
                
            

        else:
            return render(request, "log_in.html", {"name": "Customer","prompt":"Sorry UserName or Password is invalid !"})



def log_out(request):
    logout(request)
    return redirect('index')
def changepass(request):
    if request.user.is_authenticated:
        
        if request.method == "GET":
            return render(request,'changepass.html')
        elif request.method == "POST":
            password= request.POST["newpass"]
            re_password= request.POST["newpassagain"]
            
            if password != re_password:
                return render(request,'changepass.html',{'prompt':"Sorry Your Passwords Doesn't Match"})
            else:
                u = User.objects.get(username= request.user.username )
                print(u)
                u.set_password(password)
                u.save()

                if request.user.is_superuser == False:
                    obj = Customer.objects.get(user_name=request.user.username)
                    obj.password = password
                    obj.save()

                return render(request,'changepass.html',{'green_prompt':"Your Password Has been Changed"})
               
    
    else:
        return redirect('home')
    

#@login_required
#def withdraw(request):
   # if request.method == 'POST':
        #phone_number = request.POST.get('phone_number')
        #balance = request.POST.get('balance')

        # Validate phone_number
       # if not phone_number or not phone_number.isnumeric():
          #  return render(request, 'withdraw.html', {'error': 'Invalid phone number'})

        # Retrieve account from database or return an error if it doesn't exist
       # try:
           # account = Account.objects.get(phone_authorised_to_mobile_banking=phone_number)
       # except Account.DoesNotExist:
          #  return render(request, 'withdraw.html', {'error': 'Account does not exist'})

        # Retrieve Bkash account from database or create a new one if it doesn't exist
       # try:
           # bkash_account = Bkash.objects.get(phone_authorised_to_mobile_banking=phone_number)
        #except Bkash.DoesNotExist:
            #bkash_account = Bkash.objects.create(phone_authorised_to_mobile_banking=phone_number)

        # Check if there's enough balance in the account
        #if Decimal(balance) > account.balance:
            #return render(request, 'withdraw.html', {'error': 'Insufficient balance'})

        # Update account and Bkash account balance and save the changes
       # account.balance -= Decimal(balance)
      #  account.save()

      #  bkash_account.balance += Decimal(balance)
       # bkash_account.save()

        # Redirect to account details page
       # return redirect('index_after_signin')

    #return render(request, 'withdraw.html')




@login_required
def withdraw(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        balance = request.POST.get('balance')

        # Validate phone_number
        if not phone_number or not phone_number.isnumeric():
            return render(request, 'withdraw.html', {'error': 'Invalid phone number'})

        # Retrieve account from database or return an error if it doesn't exist
        try:
            account = Account.objects.get(phone_authorised_to_mobile_banking=phone_number)
        except Account.DoesNotExist:
            return render(request, 'withdraw.html', {'error': 'Account does not exist'})

        # Retrieve Bkash account from database or create a new one if it doesn't exist
        try:
            bkash_account = Bkash.objects.get(phone_authorised_to_mobile_banking=phone_number)
        except Bkash.DoesNotExist:
            bkash_account = Bkash.objects.create(phone_authorised_to_mobile_banking=phone_number)

        # Check if there's enough balance in the account
        if Decimal(balance) > account.balance:
            return render(request, 'withdraw.html', {'error': 'Insufficient balance'})

        # Update account and Bkash account balance and save the changes
        account.balance -= Decimal(balance)
        account.save()

        bkash_account.balance += Decimal(balance)
        bkash_account.save()

        # Redirect to account details page
        return redirect('index_after_signin')

    return render(request, 'withdraw.html')

def deposit(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        balance = request.POST.get('balance')
        
        # Validate phone_number
        if not phone_number or not phone_number.isnumeric():
            return render(request, 'deposit.html', {'error': 'Invalid phone number'})
        
        # Retrieve account from database or return an error if it doesn't exist
        try:
            account = Account.objects.get(phone_authorised_to_mobile_banking=phone_number)
        except Account.DoesNotExist:
            return render(request, 'deposit.html', {'error': 'Account does not exist'})
        
        # Retrieve Bkash account from database or create a new one if it doesn't exist
        try:
            bkash_account = Bkash.objects.get(phone_authorised_to_mobile_banking=phone_number)
        except Bkash.DoesNotExist:
            bkash_account = Bkash.objects.create(phone_authorised_to_mobile_banking=phone_number, balance=0)
        
        # Update account and Bkash account balance and save the changes
        account.balance += Decimal(balance)
        account.save()
        
        bkash_account.balance -= Decimal(balance)
        bkash_account.save()
        
        # Redirect to account details page
        return redirect('index_after_signin')
    
    return render(request, 'deposit.html')



def check_balance(request):
    if request.method == 'POST':
        account_id = request.POST['account_id']
        try:
            account = Account.objects.get(account_id=account_id)
            return render(request, 'balance.html', {'balance': account.balance})
        except Account.DoesNotExist:
            prompt = "Account does not exist"
            return render(request, 'check_balance.html', {'prompt': prompt})
    else:
        return render(request, 'check_balance.html')

from .models import Account

def balance(request, account_id):
    try:
        account = Account.objects.get(account_id=account_id)
        balance = account.balance
    except Account.DoesNotExist:
        balance = None

    return render(request, 'balance.html', {'balance': balance})




def transfer(request):
    if request.method == 'POST':
        from_account_id = request.POST.get('from_account_id')
        to_account_id = request.POST.get('to_account_id')
        amount = request.POST.get('amount')
        
        # Validate account ids and amount
        if not from_account_id or not from_account_id.isnumeric() or \
           not to_account_id or not to_account_id.isnumeric() or \
           not amount or not amount.isnumeric() or Decimal(amount) <= 0:
            return render(request, 'transfer.html', {'error': 'Invalid input'})
        
        # Retrieve from_account from database or return an error if it doesn't exist
        try:
            from_account = Account.objects.get(account_id=from_account_id)
        except Account.DoesNotExist:
            return render(request, 'transfer.html', {'error': 'From account does not exist'})
        
        # Retrieve to_account from database or create a new one
        to_account, created = Account.objects.get_or_create(account_id=to_account_id, defaults={'balance': 0})
        
        # Check if there's enough balance in the from_account
        if Decimal(amount) > from_account.balance:
            return render(request, 'transfer.html', {'error': 'Insufficient balance'})
        
        # Update account balances and save the changes
        from_account.balance -= Decimal(amount)
        from_account.save()
        to_account.balance += Decimal(amount)
        to_account.save()
        
        
        # Debug statements
        print(f"From Account ID: {from_account_id}, Balance: {from_account.balance}")
        print(f"To Account ID: {to_account_id}, Balance: {to_account.balance}")

       
        # Redirect to account details page
        return redirect('index_after_signin')
   
    return render(request, 'transfer.html')









