from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Member , Event
from .forms import memberForm ,eventForm ,SignUpForm
from django.contrib import messages
from django_daraja.mpesa.core import MpesaClient

# Create your views here.
def homepage(request):
    context = {}
    return render(request,'dramaapp/homepage.html', context)
def home(request):
    members = Member.objects.all()
    context={"member":members}
    return render(request,'dramaapp/home.html', context)
def contacts(request):
    context = {}
    return render(request,'dramaapp/contacts.html', context)
def productions(request):
    context = {}
    return render(request,'dramaapp/productions.html', context)
def event(request):
    context = {}
    return render(request,'dramaapp/event.html', context)  
def gallery(request):
    context = {}
    return render(request,'dramaapp/gallery.html', context)


def dashboard(request):
   
    context = {}
    
    return render(request, 'dramaapp/dashboard.html', context)

       


def login(request):
    context = {}
    return render(request,'dramaapp/login.html', context)       


def createmember(request):
    form = memberForm()
    context = {"form":form}

    if request.method == "POST":
        form = memberForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect("home")            

    return render(request, "dramaapp/form.html", context )
def readALLmember(request):
    members = Member.objects.all()
    context={"members": members}
    return render(request,"dramaapp/home.html",context)
def update_member(request, pk):
    member_obj = Member.objects.get(id=pk)
    form = memberForm(request.POST or None, request.FILES or None, instance=member_obj)

    if form.is_valid():
        form.save()
        return redirect("home")

    return render(request, "dramaapp/update.html", {"form": form})

    
def delete_member(request, pk):
    member_obj = Member.objects.get(id=pk)
    member_obj.delete()
    return redirect("home")





def createevent(request):
    form = eventForm()
    context = {"form":form}

    if request.method == "POST":
        form = eventForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect("home")            

    return render(request, "dramaapp/form.html", context )
         

def read_event(request):
    events = event.objects.all()
    context={"event":events}
    return render(request,"dramaapp/event.html",context)
def update_event(request, pk):
    events_obj = event.objects.get(id=pk)
    form = eventForm(instance=events_obj)
    if request.method == "POST":
        form = eventForm(request.POST,request.FILES, instance=events_obj)
        if form.is_valid(): 
            form.save()
            return redirect("read_event")            
    context ={"form":form}
    return render(request, "dramaapp/form.html", context)
def delete_event(request, pk):
    events_obj = event.objects.get(id=pk)
    if request.method == "POST":        
        events_obj.delete()
        return redirect("read_event")
    context={"event":events_obj}
    return render(request, "dramaapp/delete.html",context=context)




def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # By default, form.save() creates a user with is_staff=False
            # 1. Add a success message to show on the login page
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Please log in.')
            
            # 2. Redirect specifically to the 'login' URL name
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'dramaapp/signny.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('homepage')
    

def index(request):
   
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    # = '07xxxxxxxx'
   # amount = 1
   # account_reference = 'reference'
#transaction_desc = 'Description'
   # callback_url = 'https://api.darajambili.com/express-payment'
   # response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)
def mpesapayment(request):
    cl = MpesaClient()
    accountReference = "REGISTRATION FEE"
    transactionDesc = "DRAMA CLUB PAYMENT"
    callbackUrl = "https://api.darajambili.com/express-payment"

    if request.method == "POST":
        phoneNumber = request.POST.get('phonenumber')
        amount=request.POST.get('amount') # Convert to int

        response = cl.stk_push(
            phoneNumber,amount,accountReference,transactionDesc,callbackUrl)

        context = {"response": response}
        return render(request, "dramaapp/mpesapayments.html", context)

    else:
        return render(request, "dramaapp/mpesapayment.html")